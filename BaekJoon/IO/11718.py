import sys

lines = sys.stdin.readlines()
for s in lines:
    print(s.strip())

"""
raed()나 readlines()는 개행문자도 입력 받으니
입력을 끝을 내려면 EOF를 넣어 야한다
Window: ctrl+z
"""