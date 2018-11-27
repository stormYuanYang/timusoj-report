#MIT License
#Copyright (c) 2018 yangyuan
import sys

lineNo = 0
a, b, c = None, None, None
for inputStr in sys.stdin:
    if lineNo == 0:
        a = int(inputStr)
    elif lineNo == 1:
        b = int(inputStr)
    else:
        c = int(inputStr)
    lineNo += 1
    if lineNo == 3:
        lineNo = 0
        result1 = b + c
        result2 = b * c
        if result1 > result2:
            print(a - result1)
        else:
            print(a - result2)
