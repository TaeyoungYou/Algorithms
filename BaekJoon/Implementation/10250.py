import sys

test=int(sys.stdin.readline())
for _ in range(test):
    H, W, N = map(int, sys.stdin.readline().split())
    number = N // H + 1
    floor = N % H
    if floor == 0:
        floor = H
        number -= 1
    
    print(floor*100+number)