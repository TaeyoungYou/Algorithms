"""
1. X % 3 == 0, X/3
2. X % 2 == 0, X/2
3. X - 1
-> X = 1
Output: 연산을 하는 횟수

경우의 수
1. n -> n-1 -> ...
2. n -> n/2 or n/3 -> ...
"""
n = int(input())
dp_table = [0] * (n+1)  # n개의 카운트 저장 테이블
for i in range(2, n+1): # 틀림, 2부터 시작. 1은 횟수가 0이기 때문
    if i < 4:
        dp_table[i] = 1
    else:
        dp_table[i] = dp_table[i-1] + 1
        if i % 3 == 0:
            count = dp_table[i//3] + 1
            if count < dp_table[i]:
                dp_table[i] = count
        if i % 2 == 0:
            count = dp_table[i//2] + 1
            if count < dp_table[i]:
                dp_table[i] = count

print(dp_table[n])

"""
개선된 코드
"""
n = int(input())
dp = [0]* (n+1)
for i in range(2, n+1):
    dp[i]=dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
print(dp[n])