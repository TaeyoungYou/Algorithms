import sys
from functools import reduce
from collections import Counter

N=int(sys.stdin.readline())
t_facto = reduce(lambda x,y: x*y, [n+1 for n in range(1 if N==0 else N)])
total = 0
while t_facto%10==0:
    total+=1
    t_facto=t_facto//10
print(total)