# base_filter.py
from abc import ABC, abstractmethod

class BaseFilter(ABC):
    @abstractmethod
    def run(self, data):
        """运行持久项筛选算法"""
        pass

