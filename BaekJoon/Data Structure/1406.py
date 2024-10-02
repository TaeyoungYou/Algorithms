# import sys

# def input(): return sys.stdin.readline()

# word=list(input().strip())
# oper_num = int(input())

# curPos = len(word)
# for _ in range(oper_num):
#     operation = list(input().strip().split(" "))
#     if operation[0] == 'P':
#         word.insert(curPos, operation[1])
#         curPos += 1
#     elif operation[0] == 'L':
#         if curPos > 0:
#             curPos -= 1
#     elif operation[0] == 'R':
#         if curPos < len(word):
#             curPos += 1
#     elif operation[0] == 'B':
#         if curPos != 0:
#             del word[curPos-1]
#             curPos -= 1
# print("".join(word))
"""
Time Out
"""
import sys

def input(): return sys.stdin.readline()

line = list(input().rstrip())
n = int(input())

temp = []
for _ in range(n):
    operate = list(input().rstrip().split(" "))
    if operate[0] == 'L':
        if line != []:
            temp.append(line.pop())
    elif operate[0] == 'D':
        if temp != []:
            line.append(temp.pop())
    elif operate[0] == 'P':
        line.append(operate[1])
    else:
        if line != []:
            line.pop()
result=""
if line != []:
    result = result + "".join(line)
if temp != []:
    result = result + "".join(reversed(temp))
print(result)
"""
두 개의 리스트로 나눠서 해라에 힌트를 얻음
"""