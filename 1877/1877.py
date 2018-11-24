#MIT License
#Copyright (c) 2018 yangyuan
import sys

passwords = [None] * 2
i = 0
for lineStr in sys.stdin:
    passwords[i] = int(lineStr)
    i += 1
    if i == 2:
        if passwords[0] & 1 == 0:
            print("yes")
        elif passwords[1] & 1 == 1:
            print("yes")
        else:
            print("no")
        i = 0
