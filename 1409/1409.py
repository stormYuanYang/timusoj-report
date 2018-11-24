#MIT License
#Copyright (c) 2018 yangyuan
import sys
for lineStr in sys.stdin:
    H, L = map(int, lineStr.split())
    total = (H - 1) + L
    print("%d %d"%(total - H, total - L))
