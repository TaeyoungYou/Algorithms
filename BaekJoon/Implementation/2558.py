x=int(input())
y=int(input())
print(x+y)

# 다른 답
import sys

x=int(sys.stdin.readline())
y=int(sys.stdin.readline())
print(x+y)
"""
sys모듈의 표준 입력(stdin, standard input)을 사용
readline은 \n도 입력받음 / 따로 strip을 사용해 줘야함
"""