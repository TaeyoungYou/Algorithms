import sys
from collections import deque

def input(): return sys.stdin.readline()

N=int(input())

seq = list(map(int, input().rstrip().split(" ")))[:N]

for i, n in enumerate(seq):
    que = deque()
    while i < len(seq):
        if n < seq[i]:
            que.append(seq[i])
        i+=1
    if not que:
        print(-1, end=" ")
    else:
        print(que.popleft(), end=" ")
"""
Time out
최대 입력값이 1,000,000이기 때문에 O(n^2)는 시간 초과
"""
