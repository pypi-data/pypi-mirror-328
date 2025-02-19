import asyncio
import ray
import numpy as np
import talib
from ks_futu_market_api import KsFutuMarketApi
from ks_trade_api.constant import SubscribeType, Interval
import multiprocessing

# 创建队列用于传递数据
data_queue = multiprocessing.Queue()

symbol = '00700.SEHK'
interval = Interval.MINUTE

# 初始化 Ray
ray.init(ignore_reinit_error=True)

# 计算布林带的远程任务
@ray.remote
def calculate_bollinger(data):
    # 使用 TA-Lib 计算布林带
    close_prices = np.array([d['close'] for d in data])  # 假设数据中有 'close' 字段
    upper, middle, lower = talib.BBANDS(close_prices, timeperiod=20)
    return upper, middle, lower

# 使用 Ray 的任务列表来存储多个计算任务的句柄
task_futures = {}

async def process_bollinger_results():
    # 遍历所有任务句柄并获取计算结果
    for timestamp, future in list(task_futures.items()):
        if ray.wait([future], timeout=0)[0]:  # 非阻塞获取结果
            upper, middle, lower = ray.get(future)
            print(f"Timestamp: {timestamp} -> Upper: {upper[-1]}, Middle: {middle[-1]}, Lower: {lower[-1]}")
            del task_futures[timestamp]  # 处理完毕，删除该任务句柄

async def main_loop():
    while True:
        # 定期调用 process_bollinger_results，假设每隔1秒调用一次
        await process_bollinger_results()
        await asyncio.sleep(1)  # 每1秒调用一次

# 初始化 Futu API
api = KsFutuMarketApi({})

def on_book(book):
    # 假设我们从 book 数据中提取了历史价格数据（这部分需要根据实际数据结构调整）
    data = []  # 假设从 `book` 获取的数据
    # 将数据放入队列
    data_queue.put(data)
    
    # 提交计算任务并记录任务句柄
    future = calculate_bollinger.remote(data)
    task_futures[book['timestamp']] = future  # 用时间戳作为 key 存储任务句柄

# 设置回调函数
api.on_book = on_book

# 订阅市场数据
api.subscribe(symbol, [SubscribeType.BOOK, SubscribeType.K_MINUTE])

# 启动 asyncio 事件循环
loop = asyncio.get_event_loop()
loop.create_task(main_loop())  # 启动主循环
loop.run_forever()
