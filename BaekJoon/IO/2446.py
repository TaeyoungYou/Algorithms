import sys

count=int(sys.stdin.readline())
for i in range(count,1,-1):
    print(" "*(count-i)+"*"*(i*2-1))
for i in range(1, count+1):
    print(" "*(count-i)+"*"*(i*2-1))