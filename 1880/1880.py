#MIT License
#Copyright (c) 2018 yangyuan
import sys

lineNo = 0
A = {}
num = 0
for inputStr in sys.stdin:
    if lineNo & 1 == 1:
        numberStrs = inputStr.split()
        for numberStr in numberStrs:
            number = int(numberStr)
            if number not in A:
                A[number] = 1
            else:
                A[number] += 1
                if A[number] == 3:
                    num += 1
    lineNo += 1
    if lineNo == 6:
        print(num)
        num    = 0
        lineNo = 0
