import sys

def newOperate(a: int, b: int) -> int:
    return (a+b)*(a-b)

if __name__=="__main__":
    a,b=map(int, sys.stdin.readline().split())
    print(newOperate(a,b))