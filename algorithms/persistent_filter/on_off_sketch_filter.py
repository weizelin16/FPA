# algorithms/persistent_filter/on_off_sketch_filter.py
import numpy as np
from ..frequent_itemset.base_filter import BaseFilter

class OnOffSketchFilter(BaseFilter):
    def __init__(self, width=1000, depth=5):
        """初始化On-Off Sketch参数"""
        self.width = width  # Sketch的宽度（即计数器数组的长度）
        self.depth = depth  # 哈希函数的数量
        self.counters = np.zeros((self.depth, self.width), dtype=int)  # 初始化计数器数组
        self.hash_functions = [self._hash_function(i) for i in range(self.depth)]  # 初始化哈希函数

    def _hash_function(self, seed):
        """根据种子生成哈希函数"""
        np.random.seed(seed)
        a, b = np.random.randint(1, self.width), np.random.randint(0, self.width)
        return lambda x: (a * hash(x) + b) % self.width

    def add(self, item):
        """向Sketch中添加一个项"""
        for i in range(self.depth):
            index = self.hash_functions[i](item)
            self.counters[i][index] += 1

    def query(self, item):
        """查询项的估计频率"""
        min_count = float('inf')
        for i in range(self.depth):
            index = self.hash_functions[i](item)
            min_count = min(min_count, self.counters[i][index])
        return min_count

    def run(self, data):
        """对数据集执行持久项提取"""
        for item in data:
            self.add(item)
        
        # 根据设定的频率阈值提取持久项
        threshold = 10  # 设定的频率阈值，可根据需要调整
        persistent_items = {item for item in set(data) if self.query(item) >= threshold}
        return persistent_items


