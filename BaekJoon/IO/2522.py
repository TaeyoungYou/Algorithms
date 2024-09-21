import sys

count=int(sys.stdin.readline())
i = count-1
operater = -1
while i < count:
    print(" "*i+"*"*(count-i))
    if not i:
        operater *= -1
    i += operater