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
    if date not in times.keys():
        times[date] = {}
    if uid not in times[date].keys():
        times[date][uid] = []
        times[date][uid].append(gid)
    else:
        times[date][uid].append(gid)

print times

time_spred_f = open('../data_serises/time_spread.txt', 'w')
time_spred_f.write("转我是公民3文：悼念学子....\n")

for key, value in times.iteritems():
    time_spred_f.write("\ttime="+key+"\n")
    for tkey, tvalue in value.iteritems():
        time_spred_f.write("\t\tuid=" + tkey+"\n")
        for group in tvalue:
            time_spred_f.write("\t\t\tgid=" + group+"\n")
time_spred_f.close()

