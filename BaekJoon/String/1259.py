import sys

while True:
    pelin = list(sys.stdin.readline().strip())
    if pelin[0] == '0':
        break
    re_pelin = list(reversed(pelin))
    if pelin == re_pelin:
        print("yes")
    else:
        print("no")