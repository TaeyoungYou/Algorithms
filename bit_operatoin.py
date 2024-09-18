"""
AND 연산자를 이용해, 최하위 bit가 1임을 이용해 홀수를 판단
1001(9) & 1 = True -> 홀수
1000(8) & 1 = False -> 짝수
"""
num = 10
if num & 1:
    print("Odd")
else:
    print("Even")

"""
>>: 비트 이동 연산자
>> 1 은 //2와 같은 값 (소숫점 무시)
"""
print(num>>1)