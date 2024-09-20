import sys

line = sys.stdin.readline().strip()
for i in range(1, len(line)+1):
    print(line[i-1],end="")
    if not i % 10:
        print()

# 다른 답
line = sys.stdin.readline().strip()

for i in range(0,len(line),10):
    print(line[i:i+10])     # IndexError: out of range가 되지 않을까?
                            # 파이썬에서 범위를 벋어난 슬라이싱or 인덱스는 알아서 자동으로 출력 가능범위로 바꾼다