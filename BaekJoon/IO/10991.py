import sys

count=int(sys.stdin.readline())
for i in range(1,count+1):
    print(" "*(count-i)+"* "*(i-1)+"*")