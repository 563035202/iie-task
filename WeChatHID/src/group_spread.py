#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
df = pd.read_excel("../data_serises/wechat_data.xlsx")
# df = pd.read_excel("../data_serises/test_data.xlsx")

print df.columns

# print df['time']

times = {}
# for time in df['time']:
#     times[time] = {}
# print times
# for row in df:
#     print row
#     break

for index, row in df.iterrows():
    # print index
    # print row
    # break
    content = row['content']
    if not str(content).__contains__("转我是公民3文：悼念学子"):
        continue
    date = str(row['time'])
    uid = str(row['uid']).strip('\xc2\xa0')
    gid = str(row['gid']).strip()
    if gid not in times.keys():
        times[gid] = {}
    if uid not in times[gid].keys():
        times[gid][uid] = []
        times[gid][uid].append(date)
    else:
        times[gid][uid].append(date)

print times

group_spred_f = open('../data_serises/group_spread.txt', 'w')
group_spred_f.write("转我是公民3文：悼念学子....\n")

for key, value in times.iteritems():
    group_spred_f.write("\tgid="+key+"\n")
    for tkey, tvalue in value.iteritems():
        group_spred_f.write("\t\tuid=" + tkey+"\n")
        for group in tvalue:
            group_spred_f.write("\t\t\ttime=" + group+"\n")
group_spred_f.close()

