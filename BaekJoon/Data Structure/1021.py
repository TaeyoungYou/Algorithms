import sys
from collections import deque
from bisect import bisect_left, bisect_right

N,M=map(int, sys.stdin.readline().split())
que_list = deque([n+1 for n in range(N)])
goal=list(map(int,sys.stdin.readline().split()))
time=0
for g in goal:
    if len(que_list)//2 >= que_list.index(g):
        while que_list[0] != g:
            que_list.append(que_list.popleft())
            time+=1
    else:
        while que_list[0] != g:
            que_list.appendleft(que_list.pop())
            time+=1
    que_list.popleft()
print(time)
