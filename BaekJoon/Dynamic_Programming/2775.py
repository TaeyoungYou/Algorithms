import sys
apartment=[]

T=int(sys.stdin.readline())
for _ in range(T):
    floor = int(sys.stdin.readline())
    door = int(sys.stdin.readline())

    f0 = [n for n in range(1, door+1)]
    for _ in range(floor):
        for d in range(1,door):
            f0[d] = f0[d] + f0[d-1]
    print(f0[door-1])