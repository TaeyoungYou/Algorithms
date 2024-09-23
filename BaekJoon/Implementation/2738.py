import sys

N,M=map(int, sys.stdin.readline().split())
A,B=[],[]

for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))[:M]
    A.append(a)
for i in range(N):
    b = list(map(int, sys.stdin.readline().split()))[:M]
    B.append(b)

for i in range(N):
    for j in range(M):
        result = A[i][j] + B[i][j]
        print(result, end=" ")
    print()