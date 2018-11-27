#MIT License
#Copyright (c) 2018 yangyuan

# 这个代码并没有Accepted，运行时错误，暂时不知道为什么


# 国际象棋中的骑士和中国象棋中的马的走法是一样的
# 并且没有"撇脚马"的限制, 是真正的威风八面
import sys

A = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
        'g' : 7,
        'h' : 8,
    }
N = 0
for inputStr in sys.stdin:
    if N == 0:
        N = int(inputStr)
    else:
        h, v = A[inputStr[0]], int(inputStr[1])
        if (h == 1 or h == 8) or (v == 1 or v == 8):
            if (h == v) or (h + v == 9):
                print(2)
            elif (h == 1 or h == 8) and (v == 2 or v == 7) or (v == 1 or v == 8) and (h == 2 or h == 7):
                print(3)
            else:
                print(4)
        elif (h == 2 or h == 7) or (v == 2 or v == 7):
            if (h == v) or (h + v == 9):
                print(4)
            else:
                print(6)
        else:
            print(8)
        N -= 1
#try:
#    while True:
#        N = int(input())
#        while N > 0:
#            inputStr = input()
#            h, v = A[inputStr[0]], int(inputStr[1])
#            if (h == 1 or h == 8) or (v == 1 or v == 8):
#                if (h == v) or (h + v == 9):
#                    print(2)
#                elif (h == 1 and (v == 2 or v == 7)) or (h == 8 and (v == 2 or v == 7)):
#                    print(3)
#                else:
#                    print(4)
#            elif (h == 2 or h == 7) or (v == 2 or v == 7):
#                if (h == v) or (h + v == 9):
#                    print(4)
#                else:
#                    print(6)
#            else:
#                print(8)
#            N -= 1
#except:
#    pass
