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
        line.pop()
result=""
if line != []:
    result = result + "".join(line)
if temp != []:
    result = result + "".join(reversed(temp))
print(result)