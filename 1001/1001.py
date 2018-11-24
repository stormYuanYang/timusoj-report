import sys, math, time
startTimestamp = time.process_time()
squareRoots = []
for lineStr in sys.stdin:
    oneLine = lineStr.split()
    for n in oneLine:
        squareRoots.append(int(n))

i = len(squareRoots) - 1
while i >= 0:
    print("%.4f"%math.sqrt(squareRoots[i]))
    i -= 1
endTimestamp = time.process_time()
print("耗时:%.3f秒"%(endTimestamp - startTimestamp))
