import sys

nums=[0]*10

A=int(sys.stdin.readline().strip())
B=int(sys.stdin.readline().strip())
C=int(sys.stdin.readline().strip())

calc=list(str(A*B*C))
for n in calc:
    nums[int(n)] += 1

for i in nums:
    print(i)