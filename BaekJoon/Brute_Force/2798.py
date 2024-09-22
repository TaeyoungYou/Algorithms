import sys

max_cards,max_num=map(int, sys.stdin.readline().split())

cards=list(map(int, sys.stdin.readline().split()))[:max_cards]

result=0
for i in range(0, len(cards)-2):
    for j in range(i+1, len(cards)-1):
        for k in range(j+1, len(cards)):
            temp = cards[i] + cards[j] + cards[k]
            if temp <= max_num and result < temp:
                result = temp

print(result)

# 3중 루프 대신, itertools.combinations() 사용 가능