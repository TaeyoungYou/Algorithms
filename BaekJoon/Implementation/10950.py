import sys
while True:
    try:
        x,y=map(int,sys.stdin.readline().split())
        print(x+y)
    except:
        break
"""
무한히 반복되는 입출력에서 만약 잘못입력이 됬을 경우
Runtime Error가 아닌, try except를 사용해서 안전하게 break를 한다
"""