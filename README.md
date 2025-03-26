# 项目名称

## 介绍
本项目是一个用于持久项筛选和频繁项集挖掘的模块化代码框架，旨在通过实验对比不同算法的性能。
## 文档结构
project_root/
│
├── algorithms/
│   ├── __init__.py  # 用于导入不同算法模块
│   ├── persistent_filter/  # 持久项筛选算法
│   │   ├── __init__.py
│   │   ├── base_filter.py  # 定义抽象基类或接口
│   │   ├── filter1.py  # 持久项筛选算法1
│   │   └── filter2.py  # 持久项筛选算法2
│   ├── frequent_itemset/  # 频繁项集挖掘算法
│   │   ├── __init__.py
│   │   ├── base_itemset.py  # 定义抽象基类或接口
│   │   ├── algorithm1.py  # 频繁项集挖掘算法1
│   │   └── algorithm2.py  # 频繁项集挖掘算法2
│
├── config/
│   ├── experiment_config.json  # 实验配置文件，定义算法组合与实验参数
│
├── main.py  # 主控模块，用于实验管理、算法组合和性能测量
│
├── performance_metrics.py  # 性能测量模块，定义测量时间、内存等的工具函数
│
└── README.md  # 项目说明文档

## 使用方法

### 1. 添加新算法

1. 在 `algorithms/persistent_filter/` 或 `algorithms/frequent_itemset/` 目录中创建新的 Python 文件。
2. 实现 `BaseFilter` 或 `BaseItemset` 抽象基类中的 `run()` 方法。
3. 将新算法模块导入 `algorithms/__init__.py`。

### 2. 运行实验

1. 在 `config/experiment_config.json` 中配置要运行的算法组合。
2. 在终端中运行 `python main.py`。

### 3. 扩展性能测量

在 `performance_metrics.py` 中添加新的性能测量函数，并将其补充到 `main.py` 中的 `execute_pipeline()` 函数上。
