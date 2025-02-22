"""base"""

import logging
import threading
import time
import json
import itertools
import datetime
from random import choice
from typing import Union, Type, Dict, Any, List, Tuple, Literal
from concurrent.futures import Future, as_completed
from queue import PriorityQueue, Queue, Empty
from contextlib import contextmanager, suppress

import polars as pl
from tqdm import tqdm
from pytdx.hq import TdxHq_API
from pytdx.exhq import TdxExHq_API
from pytdxwrapper.config import TDX_HOSTS, TDX_CONFIG_DIR
from pytdxwrapper.mock import MockTdxHq_API


class TdxApiFactory:
    """通达信服务器工厂，负责管理tdx可用服务器，自动选择延时最小的服务器"""

    __CONFIG_DIR__ = TDX_CONFIG_DIR

    def __init__(self, tdxapi_cls: Union[Type[TdxHq_API], Type[TdxExHq_API]]) -> None:
        self._config_dir = self.__CONFIG_DIR__ / (
            "std" if issubclass(tdxapi_cls, TdxHq_API) else "ext"
        )
        if not self._config_dir.exists():
            self._config_dir.mkdir(parents=True, exist_ok=True)

        if (self._config_dir / "tdx_hosts.json").exists():
            with open(self._config_dir / "tdx_hosts.json", "r", encoding="utf-8") as fp:
                self._hosts = json.load(fp)
        else:
            self._hosts = TDX_HOSTS
        self._tdxapi_cls = tdxapi_cls
        self._stop_event = threading.Event()
        self._latency_queue: PriorityQueue[Tuple[float, str, int]] = PriorityQueue()

        self._expire_dt = 0

        if (self._config_dir / "server_latency.json").exists():
            with open(
                self._config_dir / "server_latency.json", "r", encoding="utf-8"
            ) as fp:
                server_latency = json.load(fp)
            self._expire_dt = server_latency.pop("expire_dt", 0)
            if self._expire_dt > time.time():
                for latency, host, port in server_latency["queue"]:
                    self._latency_queue.put((latency, host, port))
        self._worker = None

    def test_latency(
        self, tdx_api: Union[TdxExHq_API, TdxHq_API], host: str, port: int
    ) -> float:
        """测试服务器延时事件

        返回值:
            若服务器
        """
        try:
            start = time.perf_counter()
            if tdx_api.connect(host, port, time_out=1):
                return (time.perf_counter() - start) * 1000
        except TimeoutError:
            pass
        finally:
            tdx_api.disconnect()
        return float("inf")

    def run(self) -> None:
        """运行主函数"""

        tdx_api = self._tdxapi_cls()
        logging.info("TdxApiFactory is starting...")
        while not self._stop_event.is_set():
            if self._latency_queue.qsize() > 5 and self._expire_dt > time.time():
                with suppress(TimeoutError):
                    self._stop_event.wait(1)
                    continue
            pbar = tqdm(self._hosts)
            available_host:Dict[str,Tuple[str,str,int]] = {}
            self._latency_queue.queue.clear()
            for name, host, port in pbar:
                name = name.replace(" ", "")
                pbar.set_description_str(f"Testing {name}({host}:{port})")
                try:
                    latency = self.test_latency(tdx_api, host, port)
                    if f"{host}:{port}" not in available_host:
                        available_host[f"{host}:{port}"] = (name, host, port)
                    pbar.set_postfix_str(f"{latency:,.2f}ms")
                    if latency < 1000:
                        self._latency_queue.put((latency, host, port))
                except Exception as err:
                    pbar.set_postfix_str(str(err))

            if self._latency_queue.qsize() < 5:
                logging.error(
                    "Not enough hosts: %s, Available host: %s",
                    self._latency_queue.qsize(),
                    len(available_host),
                )
                break

            # 有效期截至至第二天9点
            self._expire_dt = (
                datetime.datetime.combine(
                    datetime.date.today(), datetime.time(hour=9, minute=0, second=0)
                )
                + datetime.timedelta(days=1)
            ).timestamp()
            self._save_latency(list(available_host.values()))

    def _save_latency(self, available_host: List[Tuple[str, str, int]]) -> None:
        """保存服务器延时信息"""
        with open(
            self._config_dir / "server_latency.json", "w", encoding="utf-8"
        ) as fp:
            json.dump(
                {"queue": self._latency_queue.queue, "expire_dt": self._expire_dt},
                fp,
                indent=4,
                ensure_ascii=False,
            )
        if len(available_host) < len(self._hosts):
            with open(self._config_dir / "tdx_hosts.json", "w", encoding="utf-8") as fp:
                json.dump(available_host, fp, indent=4, ensure_ascii=True)

    @contextmanager
    def __call__(self) -> Any:
        """获取一个api"""
        api = self._tdxapi_cls()
        try:
            while True:
                _, host, port = self._latency_queue.get()
                with suppress(TimeoutError):
                    if api.connect(host, port, time_out=1):
                        yield api
                        break
        finally:
            with suppress(Exception):
                latency = self.test_latency(api, host, port)
                if latency < 1000:
                    self._latency_queue.put((latency, host, port))

    def start(self) -> None:
        """开始维护函数"""
        if self._worker is not None and self._worker.is_alive():
            return

        self._stop_event.clear()
        self._worker: threading.Thread = threading.Thread(
            target=self.run, name=f"TdxApiFactory({id(self)})", daemon=True
        )
        self._worker.start()

    def close(self) -> None:
        """关闭维护函数"""
        self._stop_event.set()
        self._worker.join()
        self._worker = None


TdxAPIWrapper = TdxApiFactory(MockTdxHq_API)
TdxAPIWrapper.start()
# VXExTdxAPI = TdxApiFactory(TdxExHq_API)


class TdxAPITask:
    """通达信API任务"""

    def __init__(self, api_method: str, *args: Any, **kwargs: Any) -> None:
        self.api_method = api_method
        self.args = args
        self.kwargs = kwargs
        self.future: Future[Any] = Future()

    def __call__(self, api: Union[TdxHq_API, TdxExHq_API]) -> None:
        """执行任务"""
        if not self.future.set_running_or_notify_cancel():
            return
        try:
            result = getattr(api, self.api_method)(*self.args, **self.kwargs)
            self.future.set_result(result)
        except Exception as err:
            self.future.set_exception(err)


ExchangeToTDXMarket = {
    "SZ": 0,
    "SH": 1,
    "BJ": 2,
}

tick_cols = [
    "symbol",
    "name",
    "lasttrade",
    "open",
    "high",
    "low",
    "yclose",
    "volume",
    "amount",
    "ask1_p",
    "ask1_v",
    "bid1_p",
    "bid1_v",
    "ask2_p",
    "ask2_v",
    "bid2_p",
    "bid2_v",
    "ask3_p",
    "ask3_v",
    "bid3_p",
    "bid3_v",
    "ask4_p",
    "ask4_v",
    "bid4_p",
    "bid4_v",
    "ask5_p",
    "ask5_v",
    "bid5_p",
    "bid5_v",
]


class TdxAPIPool:
    """通达信API池"""

    __counter__ = itertools.count().__next__

    def __init__(self) -> None:
        self._max_size = 5
        self._workers: Dict[threading.Thread,Literal[0,1]] = {}
        self._stop_event = threading.Event()
        self._task_queue: Queue[TdxAPITask] = Queue()
        self._idle_timeout = 60
        self._lock = threading.Lock()
        self._security_list = None
        self._expire_dt = 0

    def submit(self, api_method: str, *args: Any, **kwargs: Any) -> Future[Any]:
        """提交任务"""
        task = TdxAPITask(api_method, *args, **kwargs)
        self._task_queue.put(task)
        self._adjust_worker()
        return task.future

    def _worker_run(self):
        with TdxAPIWrapper() as api:
            while not self._stop_event.is_set():
                try:
                    if self._workers[threading.current_thread()] == 1:
                        task = self._task_queue.get(timeout=self._idle_timeout)
                    else:
                        task = self._task_queue.get_nowait()
                    if task is None:
                        break
                    self._workers[threading.current_thread()] = 0
                    task(api)
                except Empty:
                    if sum(self._workers.values()) > 2:
                        time.sleep(0)
                        break
                    # heartbeat
                    if self._workers[threading.current_thread()] == 1:
                        ret = api.get_security_count(choice([0, 1]))
                        if not ret:
                            logging.warning("heartbeat failed")
                            break
                    else:
                        self._workers[threading.current_thread()] = 1

                except Exception as err:
                    logging.error("run time error: %s", err, exc_info=True)
                    break

        self._workers.pop(threading.current_thread(), None)
        logging.debug("Remove TdxApiWorker: %s", threading.current_thread().name)

    def _adjust_worker(self) -> None:
        """调整tdx api的个数"""
        if sum(self._workers.values()) > 1 or len(self._workers) >= self._max_size:
            # let other thread do it
            time.sleep(0)
            return
        t = threading.Thread(
            target=self._worker_run,
            name=f"TdxApiWorker-{self.__counter__()}",
            daemon=True,
        )
        self._workers[t] = 0
        t.start()
        logging.debug("Add TdxApiWorker: %s", t.name)

    @property
    def security_list(self) -> pl.DataFrame:
        """获取股票列表"""
        if self._security_list is not None and self._expire_dt > time.time():
            return self._security_list

        futures = []
        for market in range(0, 2):
            cnt_future = self.submit("get_security_count", market)
            cnt = cnt_future.result(5)
            if not cnt:
                logging.warning("get_security_count(%s) failed", market)
                continue
            for i in range(0, cnt, 1000):
                fu = self.submit("get_security_list", market, start=i)
                futures.append(fu)

        self._security_list = pl.concat(
            [pl.DataFrame(fu.result(5)) for fu in as_completed(futures) if fu.result(5)]
        )["symbol", "name", "volunit", "decimal_point"]
        self._expire_dt = time.time() + 24 * 60 * 60
        return self._security_list

    def current(self, *symbols: str) -> pl.DataFrame:
        """获取当前行情"""

        if len(symbols) == 0:
            symbols = self.security_list["symbol"].to_list()

        data = []
        missing = [(ExchangeToTDXMarket[symbol[-2:]], symbol[:6]) for symbol in symbols]
        batch_size = 80
        while batch_size > 0 and missing:
            futures = {}
            all_stocks, missing = missing, []
            for i in range(0, len(all_stocks), batch_size):
                futures[
                    self.submit("get_security_quotes", all_stocks[i : i + batch_size])
                ] = i

            for fu, i in futures.items():
                ret = fu.result(5)
                if not ret:
                    missing.extend(all_stocks[i : i + batch_size])
                    continue
                data.append(pl.DataFrame(ret))
            if batch_size == 1:
                print(missing)
                break
            batch_size = max(batch_size // 3, 1)
        df = (
            pl.concat(data)
            .join(self.security_list, on="symbol", how="left")
            .with_columns(
                pl.col(
                    [
                        "lasttrade",
                        "yclose",
                        "open",
                        "high",
                        "low",
                        "bid1_p",
                        "ask1_p",
                        "bid2_p",
                        "ask2_p",
                        "bid3_p",
                        "ask3_p",
                        "bid4_p",
                        "ask4_p",
                        "bid5_p",
                        "ask5_p",
                    ]
                )
                / 10 ** pl.col("decimal_point"),
                pl.col(
                    [
                        "volume",
                        "ask1_v",
                        "bid1_v",
                        "ask2_v",
                        "bid2_v",
                        "ask3_v",
                        "bid3_v",
                        "ask4_v",
                        "bid4_v",
                        "ask5_v",
                        "bid5_v",
                    ]
                )
                * pl.col("volunit"),
            )
        )[tick_cols]
        return df.sort("lasttrade")

    def history_n(
        self, symbol: str, freq: Literal["min", "day"], n: int = 100
    ) -> pl.DataFrame:
        """获取历史行情"""
        futures = []
        if freq == "min":
            cnt = (n + 1) * 4 * 60
        else:
            cnt = n + 1

        for i in range(0, cnt, 800):
            fu = self.submit(
                "get_security_bars",
                7 if freq == "min" else 4,
                ExchangeToTDXMarket[symbol[-2:]],
                symbol[:-3],
                i,
                min(800, cnt - i),
            )
            futures.append(fu)
        data = []
        for fu in as_completed(futures):
            ret = fu.result(5)
            if not ret:
                continue
            data.append(pl.DataFrame(ret))
        return (
            pl.concat(data)
            .with_columns(
                pl.col("datetime").str.strptime(pl.Datetime, "%Y-%m-%d %H:%M")
            )
            .sort("datetime")
        )


if __name__ == "__main__":
    # from vxutils import timer, loggerConfig

    tdxapi = TdxAPIPool()
    # with timer(warnning=0.0001):
    print(tdxapi.security_list)
    # time.sleep(14)
    stocks = tdxapi.security_list.filter(
        pl.col("symbol").str.starts_with("12"), pl.col("symbol").str.ends_with(".SZ")
    )["symbol"].to_list()
    # with timer(warnning=0.0001):
    print(tdxapi.current())
    # time.sleep(14)
    # with timer(warnning=0.0001):
    #    print(tdxapi.security_list)
    df = tdxapi.history_n("000002.SZ", "min", 20)
    print(
        df.with_columns(
            yclose=pl.col("close").shift(1),
            pct_change=pl.col("close").pct_change(1).over(pl.col("datetime").dt.date()),
        ).sort("datetime")
    )
    TdxAPIWrapper.close()
