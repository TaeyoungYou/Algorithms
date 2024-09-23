import sys

count=int(sys.stdin.readline())
for i in range(1, count+1):
    if i == 1:
        print(" "*(count-1)+"*")
    elif i == count:
        print("*"*(i*2-1))
    else:
        print(" "*(count-i)+"*"+" "*(i*2-3)+"*")