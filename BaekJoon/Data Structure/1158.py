from collections import deque
import sys

def input(): return sys.stdin.readline()

N, M = map(int, input().rstrip().split(" "))

que = deque()
for n in range(1, N+1):
    que.append(n)

temp = []
while que:
    for _ in range(M):
        que.append(que.popleft())
    temp.append(str(que.pop()))
print("<"+", ".join(temp)+">")