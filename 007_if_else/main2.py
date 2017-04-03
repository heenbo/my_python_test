#!/usr/bin/python3


import time

now_time = time.localtime()

now_mon = now_time.tm_mon
now_mdays = now_time.tm_mday
now_wdays = now_time.tm_wday

#print(now_mdays, now_wdays)

print("今天是%d月%d日,星期%d"%(now_mon, now_mdays, now_wdays+1))

if now_mdays <= 10:
    print("现在是上旬")
elif ((now_mdays > 10) and (now_mdays <= 20)):
    print("现在是中旬")
elif (now_mdays > 20 and now_mdays <= 31): 
    print("现在是下旬")


