import sys

num = int(sys.stdin.readline())
n_sum = 0
while num:
    n_sum += num
    num -= 1
print(n_sum)