import sys

count=int(sys.stdin.readline())
num_list=list(map(int, sys.stdin.readline().split()))[:count]
print(min(num_list),max(num_list))