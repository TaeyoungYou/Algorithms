import sys

count=int(sys.stdin.readline())
for i in range(1,count+1):
    print("*"*i+" "*2*(count-i)+"*"*i)
for i in range(count-1,0,-1):
    print("*"*i+" "*2*(count-i)+"*"*i)