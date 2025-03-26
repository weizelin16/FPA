import time
from memory_profiler import memory_usage

def measure_time(func):
    """测量函数运行时间的装饰器"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def measure_memory(func):
    """测量函数内存使用的装饰器"""
    def wrapper(*args, **kwargs):
        mem_before = memory_usage(-1, interval=0.1, timeout=1)
        result = func(*args, **kwargs)
        mem_after = memory_usage(-1, interval=0.1, timeout=1)
        print(f"Memory usage: {max(mem_after) - min(mem_before):.4f} MiB")
        return result
    return wrapper

