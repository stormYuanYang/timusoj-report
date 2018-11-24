#MIT License
#Copyright (c) 2018 yangyuan
import sys
import math

for lineStr in sys.stdin:
    N, A, B = map(int, lineStr.split())
    weight = A * B * 2 * N
    print(weight)
