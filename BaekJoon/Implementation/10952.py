import sys

while True:
    x,y=map(int, sys.stdin.readline().split())
    if not x and not y:
        break
    print(x+y)