#MIT License
#Copyright (c) 2018 yangyuan
import sys

maxProblemCount = 4 * 60 // 45
for lineStr in sys.stdin:
    n = int(lineStr)
    if 12 - n <= maxProblemCount:
        print("YES")
    else:
        print("NO")
