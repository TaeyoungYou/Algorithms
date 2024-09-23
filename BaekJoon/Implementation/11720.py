import sys

count=int(sys.stdin.readline())
num_list=list(map(int,sys.stdin.readline().rstrip()))[:count]
print(sum(num_list))