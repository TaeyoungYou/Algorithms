"""
n = 2와 5로 나누어 떨어지지 않음
1로만 이루어진 숫자: 1, 11, 111, 1111, 11111, ...

1. 임의의 숫자 11,111... -> Overflow 문제 (모듈러 산술 필요)
2. %n == 0 -> 배수 찾기
3. 1의 갯수 -> 자릿수

모둘러 연산(Modular Arithmetic)
    mod m일 때, 항상 0 ~ (m-1)의 범위를 가지는 값을 얻음
    음수일 때, 양수로 생각하고 mod 하고, + m

    17 mod 5 = 2
    -1 mod 11 = 1 mod 11 = 1, -1 + 11 = 10

합동 (Congruent)
    (a mod n) = (b mod n), mod n에 대해 합동

Property
    [(a mod n)+(b mod n)] mod n = (a+b) mod n
    [(a mod n)*(b mod n)] mod n = (a*b) mod n

Extra:
    a (a < n)= a mod n
"""

def myCode():
    while(True):
        try:
            n = int(input())
        except:
            break
        num = 1
        count = 1
        while num % n != 0:
            num = num * 10 + 1
            count += 1
        print(count)

"""
참고: https://velog.io/@pakxe/PSJS-4375%EB%B2%88-1
모듈러 연산 공식 이해
"""

def Best():
    while True:
        try:
            n = int(input())
        except:
            break
        num = 1 
        count = 1
        while num % n != 0:
            num = (num*10+1)%n
            count += 1
        print(count)

Best()