import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import acf


# 读取数据并进行初步分析
def load_and_analyze_data(file_path):
    # 加载数据
    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # 确保时间戳字段是日期时间类型
    df.set_index('timestamp', inplace=True)

    # 查看数据的时间分布
    df['value'].resample('T').count().plot()  # 'T' 表示按分钟重采样并计数
    plt.title('Transaction Count per Minute')
    plt.xlabel('Time')
    plt.ylabel('Transaction Count')
    plt.show()

    return df


# 设定初始时间窗口并重采样数据
def resample_data_with_windows(df, time_windows):
    for window in time_windows:
        resampled_data = df['value'].resample(window).sum()
        resampled_data.plot(label=f'{window} window')

    plt.title('Resampled Data with Different Time Windows')
    plt.xlabel('Time')
    plt.ylabel('Transaction Count')
    plt.legend()
    plt.show()


# 性能测试与自相关分析
def autocorrelation_analysis(df, time_windows):
    for window in time_windows:
        resampled_data = df['value'].resample(window).sum()
        autocorr = acf(resampled_data, fft=True)
        plt.plot(autocorr, label=f'{window} window')

    plt.title('Autocorrelation for Different Time Windows')
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation')
    plt.legend()
    plt.show()


# 动态时间窗口调整
def dynamic_window_selection(df, short_term='10S', long_term='1H'):
    short_resampled = df['value'].resample(short_term).sum()
    long_resampled = df['value'].resample(long_term).sum()

    # 根据短期波动和长期趋势调整时间窗口
    dynamic_window = []
    for i in range(len(short_resampled)):
        if short_resampled.iloc[i] > short_resampled.mean() * 1.5:
            dynamic_window.append(short_term)
        else:
            dynamic_window.append(long_term)

    return dynamic_window


# 主函数，执行以上步骤
def main():
    file_path = 'your_data.csv'  # 替换为你的数据路径
    df = load_and_analyze_data(file_path)

    # 定义时间窗口
    time_windows = ['10S', '1T', '5T', '1H']  # 10秒, 1分钟, 5分钟, 1小时

    # 重采样并绘制不同时间窗口的效果
    resample_data_with_windows(df, time_windows)

    # 进行自相关分析
    autocorrelation_analysis(df, time_windows)

    # 选择动态时间窗口
    dynamic_windows = dynamic_window_selection(df)
    print("Dynamic windows selected:", dynamic_windows)

    # 使用选定的时间窗口对数据进行最终处理
    selected_window = '1T'  # 假设选择了 1 分钟的窗口进行进一步处理
    final_resampled_data = df['value'].resample(selected_window).sum()

    # 对数据进行下一步分析或训练模型
    # 例如，训练一个频繁项集挖掘模型

    # 保存处理后的数据
    final_resampled_data.to_csv('resampled_data.csv')
    print("Final resampled data saved to 'resampled_data.csv'")


# 运行主函数
if __name__ == "__main__":
    main()
