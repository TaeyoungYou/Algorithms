import sys

M, N = map(int, sys.stdin.readline().split())

numbers=[1]*(N+1)
numbers[0], numbers[1] = 0, 0

for i in range(2,N+1):
    if numbers[i]:
        for j in range(i*2,N+1,i):
            numbers[j] = 0
numbers = numbers[M:N+1]
for i, value in enumerate(numbers, start=M):
    if value:
        print(i)

# 에라토스테네스의 체
# 개선 방법: 소수의 배수는 그 소수의 제곱근까지만 확인하면 됨