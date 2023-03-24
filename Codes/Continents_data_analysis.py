import pandas as pd
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
continent_names = [
'亚洲',
'北美洲',
'大洋洲',
'欧洲',
'亚洲',
'欧洲',
'南美洲'
]
province_confirmedCount=[
33610,
1069424,
6762,
3784,
16169,
10406,
16023
]
province_curedCount = [
8373,
153947,
5600,
3134,
1244,
1238,
8580
]
province_deadCount=[
1075,
62996,
92,
90,
15,
261,
227
]
fig,ax = plt.subplots(nrows=2,ncols=2,figsize=(20,15))
ax[0][0].barh(continent_names,province_confirmedCount,color = 'orange',height = 0.2,label='各大洲确诊人数')
ax[0,0].legend()
ax[0][1].bar(continent_names,province_curedCount,color='g',label='各大洲治愈人数',width=0.2)
ax[0][1].legend()
ax[1][0].bar(continent_names,province_deadCount,color = 'r',label='各大洲死亡人数',width = 0.2)
ax[1][0].legend()
ax[1][1].bar(['确诊','治愈','死亡'],[province_confirmedCount[1],province_curedCount[1],province_deadCount[1]],label='北美洲疫情人数统计',width=0.2)
plt.legend()
plt.xlabel('更新时间：2020-5-1')
fig.savefig(r'D:\Python\数学建模大作业\pictures\Continents_data_analysis.png',dpi = 180)
plt.show()