import sys

def div_sum(num: list):
    for n in range(num):
        temp = list(map(int,str(n)))
        if num == (n+sum(temp)):
            return n
    return 0            

if __name__=="__main__":
    num=int(sys.stdin.readline())
    print(div_sum(num))