"""
브루트 포스로 가능하지만 시간 초과로
유클리드 호제법을 알아야 한다
a%b=r
b%r=r2
r%r2=0
GCD = r

LCM = (a*b)/GCD
"""

import sys

a,b=map(int, sys.stdin.readline().split())

temp1 = a
temp2 = b
while temp2 != 0:
    temp1, temp2 = temp2, temp1%temp2
GCD = temp1
LCM = (a*b)//GCD
print(GCD)
print(LCM)