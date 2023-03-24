import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
# 一、首先读取数据，整理好想要用来画图的数据 文件：：D:\Python\数学建模大作业\Datas\2.ncov-data-master\china.patients.dxy.csv
# 这里需要的是性别列表 和 年龄分布列表
df = pd.read_csv(r"D:\Python\数学建模大作业\Datas\2.ncov-data-master\china.patients.dxy.csv", engine='python')

df.columns = df.loc[1]

df.loc[407, 'gender'] = 'female'
genders = list(df['gender'][2:-1])
sexs = []
for gender in genders:
    if gender == 'male' or 'female' or 'NaN':
        sexs.append(gender)
counts_1 = list(map(lambda x: x[1], Counter(sexs).items()))
print(counts_1)

# plt.scatter(range(0,len(df['age'][2:-1])),df['age'][2:-1],linewidths=0.01,edgecolors='r')
# plt.show()
## 0 ~ 100  20为一组
age_0_20 = []
age_20_40 = []
age_40_60 = []
age_60_80 = []
age_80_100 = []
age_unknown = []
for age in df['age'][2:-1]:
    if type(age) == float:
        age_unknown.append(age)
    else:
        age = eval(age)
        if 20 >= age > 0:
            age_0_20.append(age)
        elif 20 < age <= 40:
            age_20_40.append(age)
        elif 40 < age <= 60:
            age_40_60.append(age)
        elif 60 < age <= 80:
            age_60_80.append(age)
        elif 80 < age <= 100:
            age_80_100.append(age)

# 二、画图
labels = ["未知", '男', '女']
explode = [0, 0, 0.05]
colors = ["red", "yellowgreen", "lightskyblue"]
plt.pie(
    counts_1,
    explode,
    labels,
    colors,
    radius=0.9,
    autopct="%.2f%%",
    shadow=False,
    startangle=90
)
plt.legend(loc="upper right")
plt.axis("equal")
plt.savefig(r'D:\Python\数学建模大作业\pictures\sex_analysis.png', dpi=180)

plt.figure(figsize=(10, 8))
plt.pie(
    [len(age_unknown), len(age_0_20), len(age_20_40), len(age_40_60), len(age_60_80), len(age_80_100)],
    labels=['未知年龄', '20岁以下', '20~40岁', '40~60岁', '60~80岁', '80~100岁'],
    explode=[0, 0, 0, 0.03, 0, 0],
    startangle=90,
    radius=0.9,
    autopct="%.2f%%",
    center=(0, -4)
)
plt.legend(loc='lower center', ncol=6)
plt.savefig(r'D:\Python\数学建模大作业\pictures\age_analysis.png', dpi=180)
