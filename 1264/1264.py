#MIT License
#Copyright (c) 2018 yangyuan
import sys

for lineStr in sys.stdin:
    N, M = map(int, lineStr.split())
    count = N * (M + 1)
    print("%d"%count)
