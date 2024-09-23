import sys

word=list(sys.stdin.readline().strip())

for c in word:
    if c == c.upper() and c != c.lower():
        print(c.lower(),end="")
    else:
        print(c.upper(),end="")

# 다른 풀이
c.isupper()     # 대문자인지 확인
c.swapcase()    # 대소문자 각 문자 스위치
