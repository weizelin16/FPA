# base_itemset.py
from abc import ABC, abstractmethod

class BaseItemset(ABC):
    @abstractmethod
    def run(self, data):
        """运行频繁项集挖掘算法"""
        pass

