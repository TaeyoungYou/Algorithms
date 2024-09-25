import sys

answer = 0
for i in range(3):
    temp = sys.stdin.readline().strip()
    if temp not in ['FizzBuzz','Fizz','Buzz']:
        answer = int(temp)+3-i
if answer % 15 == 0:
    print('FizzBuzz')
elif answer % 3 == 0:
    print('Fizz')
elif answer % 5 == 0:
    print('Buzz')
else:
    print(answer)

"""
3의 배수와 5배수들은 절대로 3개 연속 숫자가 나올 수 없음
그러므로 셋 중, 하나는 숫자라는 것
"""