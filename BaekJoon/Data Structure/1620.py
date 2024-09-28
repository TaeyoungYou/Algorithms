import sys

N,M=map(int,sys.stdin.readline().split())
poket_list=list(sys.stdin.readline().rstrip() for _ in range(N))
ques_list=list(sys.stdin.readline().rstrip() for _ in range(M))
poket_dict = dict(zip(poket_list,[str(n+1) for n in range(N)]))
poket_dict.update(dict(zip([str(n+1) for n in range(N)], poket_list)))
for q in ques_list:
    print(poket_dict[q])
