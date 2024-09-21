import sys

count=int(sys.stdin.readline())
i = 0
while count:
    print(" "*i+"*"*count)
    i += 1
    count -= 1