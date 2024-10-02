import sys
from collections import deque

def input(): return sys.stdin.readline()

N = int(input())
que = deque()

for _ in range(N):
    oper = list(input().rstrip().split(" "))
    if oper[0] == 'push_front':
        que.appendleft(oper[1])
    elif oper[0] == 'push_back':
        que.append(oper[1])
    elif oper[0] == 'pop_front':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif oper[0] == 'pop_back':
        if que:
            print(que.pop())
        else:
            print(-1)
    elif oper[0] == 'size':
        print(len(que))
    elif oper[0] == 'empty':
        print(0 if que else 1)
    elif oper[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif oper[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)