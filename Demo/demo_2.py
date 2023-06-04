# -*- coding = utf-8 -*-
# @Time : 2023/6/4 21:17
# @Author : Cat.E
# @File : demo_2.py
# @Software: PyCharm

import pandas as pd

# 读取测试数据
df = pd.read_csv('fyx_chinamoney.csv')

# 获取第一列数据
data = df.iloc[:, 0]

# 定义批次大小
batch_size = 80

# 拆分数据列成多个批次
batches = [data[i:i+batch_size].tolist() for i in range(0, len(data), batch_size)]

# 打印输出每个批次的数据
for i, batch in enumerate(batches):
    print(f"批次 {i+1}:")
    for item in batch:
        print(item)
    print()
