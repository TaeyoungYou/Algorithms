import sys

days = {28:[2],
        30:[4,6,9,11],
        31:[1,3,5,7,8,10,12]}
weeks = {0:"SUN",
         1:"MON",
         2:"TUE",
         3:"WED",
         4:"THU",
         5:"FRI",
         6:"SAT"}

mon,day=map(int,sys.stdin.readline().split(" "))
total_days = day
for m in range(1, mon):
    if m in days.get(31):
        total_days += 31
    elif m in days.get(30):
        total_days += 30
    else:
        total_days += 28
print(weeks.get(total_days%7))

# 개선 코드
# map에서 값을 가져 올때
for key, value in days.items():
    if m in value:
        total_days += key

# list를 사용
["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
[31,28,31,30,31,30,31,31,30,31,30,31]