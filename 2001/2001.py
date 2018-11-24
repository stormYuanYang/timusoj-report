#MIT License
#Copyright (c) 2018 yangyuan
import sys

index = 0
a1, b1, b2, a3 = None, None, None, None
for lineStr in sys.stdin:
    if index == 0:
        a1, b1 = map(int, lineStr.split())
    elif index == 1:
        _, b2 = map(int, lineStr.split())
    elif index == 2:
        a3, _ = map(int, lineStr.split())

    index += 1
    if index == 3:
        print("%d %d"%(a1 - a3, b1 - b2))
        index = 0
