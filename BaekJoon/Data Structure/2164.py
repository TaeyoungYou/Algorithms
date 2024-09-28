import sys
from collections import deque

deck=list(n for n in range(1,int(sys.stdin.readline())+1))
deck_que=deque(deck)
dump=True
while len(deck_que) != 1:
    if dump:
        deck_que.popleft()
        dump=False
    else:
        deck_que.append(deck_que.popleft())
        dump=True
print(deck_que.popleft())
"""
더 효율적인
while len(deck_que) > 1:
    deck_que.popleft()
    deck_que.append(deck_que.popleft())
어차피 번갈아가면서 하니
"""