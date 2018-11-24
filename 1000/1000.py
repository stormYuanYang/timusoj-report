import sys

for lineStr in sys.stdin:
    line = lineStr.split()
    a, b = int(line[0]), int(line[1])
    print(a + b)
