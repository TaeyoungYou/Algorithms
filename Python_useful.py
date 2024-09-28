# 곱셈 n << 1 = n * 2
print(5 << 1)
# 나눗셈 n >> 1 = n // 2    소수점 무시
print(5 >> 1)

#짝수, 홀수     짝수일 경우: 0, 홀수: 1
print(4&1)

#리스트
#list comprehension
print([n for n in range(20) if n&1])    # 홀수만
# sorted 특정 키 설정
print(sorted([('taeyoung',175),('seoyoung',162),('jinhee',170)],key=lambda x: x[1], reverse=True))
# insert, remove 경우 O(n) 소요, set과 list comprehension 사용
temp = [1,2,2,3,3,5,5,5]
remove_set = {3,5}
print([n for n in temp if n not in remove_set])

#딕셔너리
import collections
a=[1,2,3,3,4,5,5,5]
counter_dic = collections.Counter(a)
print(counter_dic)
print(counter_dic.most_common())

#Set
data = set([1,1,2,3,3,4,5,5,5])
print(data)
data2 = set([3,4,5])
print(data | data2)     # 합집합
print(data & data2)     # 교집합
print(data - data2)     # 차집합

#람다
def add(a,b):
    return a+b
print(add(b=7,a=3))
print((lambda a,b: a+b)(b=7,a=3))   # 똑같은 동작

#자료구조
#Stack: 기본 리스트로 구현
stack=[]
stack.append(5) # 뒤에 요소 넣기 = push()
stack.append(1)
print(stack.pop())  # 뒤에 요소 빼기 = pop()
print(stack.pop())

#Queue: collectoins의 deque
from collections import deque
que = deque()
que.append(5)
que.append(1)
print(que)
que.popleft()
print(que)

#Heap
import heapq    # heapq는 리스트를 힙처럼 다룰 수 있도록 도와줌
heap=[]
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 7)
print(heap)     # heap 사용법

heap=[3,6,1,2,9]
heapq.heapify(heap)
print(heap)     # 리스트를 heap에 넣는 법

heap=[3,6,1,2,9]
temp=[]
for h in heap:
    heapq.heappush(temp, (-h, h))
print(temp[0][1])   # 최대힙으로 사용 법

heap=[5,2,3,1,4]
heapq.heapify(heap)
print(list(heapq.heappop(heap) for _ in range(len(heap))))

#Hash
temp_dict = {}

#내장 함수
print(sum([1,2,3]))
print(min([3,1,2]))
print(max([2,3,1]))
print(sorted([2,3,1]))
print(sorted([2,3,1], reverse=True))
print(sorted([('tae',175),('seo',162),('a',160)], key=lambda t: t[1], reverse=True))
print(list(zip(['hello','hi','what'],[1,2,3])))

#itertools
import itertools
data = ['a','b','c']
print(list(itertools.permutations(data,2)))     # 가능한 모든 조합
print(list(itertools.combinations(data,2)))     # 순서를 고려한 모든 조합
print(list(itertools.product(data,repeat=2)))   # 가능한 모든 조합 및 자신을 포함
print(list(itertools.combinations_with_replacement(data,2)))    # 순서를 고려한 모든 조합 및 자신을 포함

import bisect
a=[1,2,4,4,8]
print(bisect.bisect_left(a, 4), bisect.bisect_right(a,4))   # 값이 다르면 이미 값이 존재

#functools
import functools
print(sum(list(n+1 for n in range(10))))
print(functools.reduce(lambda t,x: t+x, list(n+1 for n in range(10))))