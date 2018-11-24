import random
totalSize = 256 * 1024
dataNum = totalSize // 8
dataNum //= 2
f = open("./1001input.txt", "w")
i = 1
random.seed()
while i <= dataNum:
    randomInt = random.randint(0, 1000000000000000000)
    f.write(str(randomInt))
    if i % 10 == 0:
        f.write("\n")
    else:
        f.write(" ")
    i += 1

f.write(str(0))
f.close()
