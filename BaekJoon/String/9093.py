import sys
input=sys.stdin.readline

lines=int(input())
store_lines=[]*lines
for _ in range(lines):
    store_lines.append(input().strip())
for l in store_lines:
    for word in list(l.split(" ")):
        print("".join(reversed(word)), end=" ")
    print()