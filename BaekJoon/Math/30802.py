import sys

people=int(sys.stdin.readline().strip())
T_size = list(map(int, sys.stdin.readline().strip().split()))[:6]
T, P = map(int,sys.stdin.readline().strip().split())

total_T = 0
for t in T_size:
    if t == 0 or t % T == 0:
        total_T += (t//T)
    else:
        total_T += ( t//T + 1)

total_P_set = people//P
total_P = people%P
print(total_T)
print(total_P_set,total_P)