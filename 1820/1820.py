#MIT License
#Copyright (c) 2018 yangyuan
import sys, math

for lineStr in sys.stdin:
    n, k = map(int, lineStr.split())
    if n <= k:
        print(2)#至少需要2分钟(因为牛排有两面)
    else:
        time = math.ceil(n * 2 / k)
        print(time)
