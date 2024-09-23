import sys

num_list=list(map(int, sys.stdin.readline().split()))[:5]
total = 0
for i in num_list:
    total += i**2
print(total%10)