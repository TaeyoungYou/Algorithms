import sys

count=int(sys.stdin.readline())
for i in range(count):
    x,y=map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {x+y}")