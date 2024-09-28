import sys
from collections import Counter
from bisect import bisect_left, bisect_right

N=int(sys.stdin.readline())
card=sorted(list(map(int,sys.stdin.readline().strip().split()))[:N])
M=int(sys.stdin.readline())
own=list(map(int,sys.stdin.readline().strip().split()))[:M]
count_dic=dict(Counter(card))
print(*[count_dic[o] if bisect_left(card, o) != bisect_right(card, o) else 0 for o in own])

"""
count_dic.get(o, 0) : 만약 찾을 수 없을 경우, 0
"""