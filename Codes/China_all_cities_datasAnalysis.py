from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as font_manager
import pandas as pd
df = pd.read_csv('D:\Python\数学建模大作业\Datas\\1.COVID'\
                 '-19-master\\archived_data\\archived_time_s'\
                 'eries\\time_series_2019-ncov-Confirmed.csv',
                 engine='python'
)
# 读取中国城市名
cities = list(df['Province/State'][0:30])
# print(cities)

# 读取确诊人数
confirmed = {}
for i in range(0,30):
    confirmed[cities[i]] = []
    for j in list(df.loc[i])[4:49]:
        confirmed[cities[i]].append(j)
#print(len(confirmed['Anhui']))

# 读取时间以及设置时间格式
dates = []
for item in list(df.columns[4:49]):
    [a,b] = item.split(' ')
    dates.append(a)

new_dates = []
for i in dates:
    [month,day,year] = i.split('/')
    [month,day,year] = [int(month),int(day),int(year)]
    if month != 2002:
        pass
    else:
        month = 2
    new_dates.append('%d月%d日'%(int(month),int(day)))

finall_dates = []
in_dex = []
for i,v in enumerate(new_dates):
    if new_dates.index(v) == i:
        finall_dates.append(v)
    else:
        finall_dates.append('abc')
        in_dex.append(i)
    for key in confirmed.keys():
        for x in in_dex:
            confirmed[key][x] = 'abc'
while 'abc' in finall_dates:
    finall_dates.remove('abc')
for key in confirmed.keys():
    while 'abc' in confirmed[key]:
        confirmed[key].remove('abc')
print(cities)
print(confirmed)
print(finall_dates)
# # 绘图11
# # print(df.loc[0])
# # for key in confirmed.keys():
# plt.figure(figsize=(30,20))
# # my_font = font_manager.FontProperties(fname='C:\\Windows\\Fonts\\msyh.ttc')
# for key in confirmed.keys():
#     colors =['blue','orange','yellow','red','black','green']
#     if key != 'Hubei':
#         plt.bar(finall_dates,confirmed[key],width=0.5,color=colors[np.random.randint(0,5)],label=key)
#     else:
#         plt.figure()
#         plt.bar(finall_dates, confirmed['Hubei'], width=0.5, label='Hubei')
#     # plt.bar(finall_dates,confirmed['Shanghai'],width=0.5,color='blue',label='上海')
# plt.title("安徽省和上海市确诊人数变化")
# plt.xticks(finall_dates,finall_dates,rotation = 90)
# plt.yticks(range(0,100))
# plt.grid(alpha =0.2)
# plt.legend(loc='upper left',fontsize = 10,labelspacing=0.1,ncol = 4)
# plt.show()
# # def plot_bar(x,y):
# #     plt.gca()
# #     plt.bar(x,y)
# #     plt.show()
# # plot_bar(finall_dates,confirmed['Shandong'])
# 湖北索引值：12

# colors_HEX = []
# fo = open("D:\\我的文档\\colors-master\\hex-codes.txt",'r+')  # https://github.com/jonasjacek/colors
# tex = fo.readlines()
# for item in tex[0:-1:10]:
#     colors_HEX.append(item[0:7])
# fo.close()

colors_HEX = ['#ffff00','#0000d7','#00afff','#870000','#626262','#5f87d7']
ls = [(0,6),(6,12),(13,19),(19,25),(25,31),(12,13)]
ls_1 = [(0,2),(2,4),(4,6)]
for a,b in ls_1:
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(20,12), sharex=True)
    ax[0].set_title("各省确诊人数变化")
    ax[0].set_ylabel("确诊人数（\人）")
    ax[1].set_ylabel("确诊人数（\人）")
    for tuple_ in ls[a:b]:
        (f,g) = tuple_
        e = 1
        if 12 not in range(f,g):
            x = 0
            y = 0
            if (ls.index((f,g)) + 1) % 2 == 0:
                m = 0
            else:
                m = 1
            for key in list(confirmed.keys())[f:g]:
                ax[m].bar([q + y * 0.1 - 0.3 for q in range(len(finall_dates))], confirmed[key], width=0.1,color=colors_HEX[x], label=key)
                ax[m].legend(loc='upper left', ncol=2,fontsize=8)
                ax[m].grid(alpha = 0.4)
                xsticks = list(range(0, len(finall_dates), 2))
                xlabels = [finall_dates[i] for i in xsticks]
                ax[0].set_xticks(xsticks)
                ax[0].set_xticklabels(xlabels)

                x += 1
                y += 1
        else:   #湖北
            # fig1 = plt.gcf()
            # fig1.axes[0].bar(finall_dates, confirmed['Hubei'], width=0.8, color='orange', label='Hubei')         #### 为什么这三行代码不能显示出最后哪个图像？？？？
            # fig1.axes[0].legend(loc='upper left')
            # ax1 = plt.gca()
            # ax1.plot(range(0,4),range(0,4))
            # plt.show()
            fig1 = plt.gcf()
            fig1.axes[0].scatter(range(0,25),confirmed['Hubei'],color='orange',linewidth=1,label = 'Hubei')
            fig1.axes[0].legend(loc='upper left')
            fig1.axes[0].grid()
            fig1.savefig(fname='D:\Python\数学建模大作业\pictures/figue_3.png',dpi=180)
plt.show()


# fig,ax = plt.subplots()
# ax1 = plt.gca()
# print(ax)
# print(ax1)

# x = 0
# y = 0
# fig, ax = plt.subplots(nrows=2, ncols=1,figsize = (20,8),sharex=True, sharey=False)
# ax[0].set_title("各省确诊人数变化1")
# for key in list(confirmed.keys())[0:6]:
#     if key != 'Hubei':
#         ax[1].bar([i + y * 0.1 - 0.3 for i in range(len(finall_dates))],confirmed[key],width = 0.1,color=colors_HEX[x],label =key)
#         ax[1].legend(loc='upper left', ncol=4, fontsize=6)
#     else:
#         ax[0].bar([i + y * 0.15 for i in range(len(finall_dates))],confirmed[key],width = 0.15,color=colors_HEX[x],label = key)
#         ax[0].legend(loc='upper left', ncol=1, fontsize=10)
#     x += 1
#     y += 1


# fig,ax = plt.subplots(nrows=2,ncols=1,figsize=(20,10))
# ax[0].bar([i for i in range(len(finall_dates))],confirmed['Anhui'],width = 0.3,color=colors_HEX[22],label ='安徽')
# ax[0].legend()
# ax[0].set_xticks(list(range(0,len(finall_dates),2)))
# ax[0].set_xticklabels([finall_dates[i] for i in list(range(0,len(finall_dates),2))])
#
# ax[0].bar([i+0.3 for i in range(len(finall_dates))],confirmed['Shanghai'],width = 0.3,color=colors_HEX[2],label ='上海')
# ax[0].legend(loc = 'upper left')
# ax[0].set_xticks(list(range(0,len(finall_dates),2)))
# ax[0].set_xticklabels([finall_dates[i] for i in list(range(0,len(finall_dates),2))])
#
# plt.show()

'''
plt.figure()
plt.pie([1,1,2,3])
'''
