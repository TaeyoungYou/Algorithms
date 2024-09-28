import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
data = sorted(list(map(int, sys.stdin.readline().strip().split()))[:N])
M = int(sys.stdin.readline())
comp_data = list(map(int, sys.stdin.readline().strip().split()))[:M]
for n in comp_data:
    print(1 if bisect_left(data,n) != bisect_right(data,n) else 0)