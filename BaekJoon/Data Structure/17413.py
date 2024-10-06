import sys
from collections import deque

def input(): return sys.stdin.readline()

stack = []
lines = list(input().rstrip())

bracket_in = False
for w in lines:
    if bracket_in and w != '>':
        print(w,end="")
    else:
        if w in ['<',' ']:
            while stack:
                print(stack.pop(),end="")
            print(w, end="")
            if w == '<':
                bracket_in = True
        elif w == '>':
            print(w, end="")
            bracket_in = False
        else:
            stack.append(w)
while stack:
    print(stack.pop(), end="")