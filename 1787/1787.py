#MIT License
#Copyright (c) 2018 yangyuan
import sys

index = 0
k, n = None, None
a = [None] * 100
for lineStr in sys.stdin:
    if index == 0:
        k, n = map(int, lineStr.split())
    elif index == 1:
        strList = lineStr.split()
        i = 0
        for oneStr in strList:
            a[i] = int(oneStr)
            i += 1
    index += 1

    if index == 2:
        index  = 0
        i      = 0
        jamNum = 0
        while i < n:
            jamNum += a[i]
            if jamNum > 0:
                jamNum -= k
                if jamNum < 0:
                    jamNum = 0
            i += 1
        print(jamNum)
