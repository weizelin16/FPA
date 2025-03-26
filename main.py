import json
import importlib
from performance_metrics import measure_time, measure_memory

def load_algorithm(module_name, class_name):
    """动态加载算法模块"""
    module = importlib.import_module(module_name)
    algorithm_class = getattr(module, class_name)
    return algorithm_class()

def run_experiment(config_file):
    """根据配置文件运行实验"""
    with open(config_file) as f:
        config = json.load(f)

    filter_module = config['persistent_filter']['module']
    filter_class = config['persistent_filter']['class']
    itemset_module = config['frequent_itemset']['module']
    itemset_class = config['frequent_itemset']['class']

    filter_algorithm = load_algorithm(filter_module, filter_class)
    itemset_algorithm = load_algorithm(itemset_module, itemset_class)

    data = ...  # 数据加载和预处理
    filtered_data = filter_algorithm.run(data)
    itemsets = itemset_algorithm.run(filtered_data)

    # 运行实验并测量性能
    @measure_time
    @measure_memory
    def execute_pipeline():
        filtered_data = filter_algorithm.run(data)
        itemsets = itemset_algorithm.run(filtered_data)
        return itemsets
    
    execute_pipeline()

if __name__ == "__main__":
    run_experiment("config/experiment_config.json")

