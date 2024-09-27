# import sys

# class Number:
#     def __init__(self, value):
#         self.value = value
#         self.time = 1
    
#     def __eq__(self, other):
#         if isinstance(other, Number):
#             return other.value == self.value
#         return False
    
#     def __hash__(self):
#         return hash(self.value)
    
#     def __str__(self):
#         return str(self.value)

# class Merge:
#     def __init__(self):
#         pass
    
#     def __merge(self, temp1: list[Number], temp2: list[Number]):
#         i,j = 0,0
#         res_list = []
#         while i<len(temp1) and j<len(temp2):
#             if temp1[i].value < temp2[j].value:
#                 res_list.append(temp1[i])
#                 i+=1
#             else:
#                 res_list.append(temp2[j])
#                 j+=1
        
#         while i<len(temp1):
#             res_list.append(temp1[i])
#             i+=1
#         while j<len(temp2):
#             res_list.append(temp2[j])
#             j+=1
#         return res_list
    
#     def __merge_time(self, temp1: list[Number], temp2: list[Number]):
#             i,j = 0,0
#             res_list = []
#             while i<len(temp1) and j<len(temp2):
#                 if temp1[i].time > temp2[j].time:
#                     res_list.append(temp1[i])
#                     i+=1
#                 else:
#                     res_list.append(temp2[j])
#                     j+=1
            
#             while i<len(temp1):
#                 res_list.append(temp1[i])
#                 i+=1
#             while j<len(temp2):
#                 res_list.append(temp2[j])
#                 j+=1
#             return res_list

#     def merge_sort(self, temp: list[Number]):
#         if len(temp) <= 1:
#             return temp
#         mid_pos = len(temp)//2
#         left = self.merge_sort(temp[:mid_pos])
#         right = self.merge_sort(temp[mid_pos:])

#         return self.__merge(left, right)
    
#     def merge_sort_time(self, temp: list[Number]):
#         if len(temp) <= 1:
#             return temp
#         mid_pos = len(temp)//2
#         left = self.merge_sort_time(temp[:mid_pos])
#         right = self.merge_sort_time(temp[mid_pos:])

#         return self.__merge_time(left, right)

# def make_set(temp: list[Number]):
#     temp_set: set[Number] = set()
#     for t in temp:
#         t.time = 0
#         temp_set.add(t)
#     for i in temp_set:
#         for j in temp:
#             if i == j:
#                 i.time += 1
#     return list(temp_set)
    

# if __name__=="__main__":
#     num = int(sys.stdin.readline())
#     num_list: list[Number] = []
#     for _ in range(num):
#         num_list.append(Number(int(sys.stdin.readline())))

#     #산술 평균
#     total = 0
#     for i in num_list:
#         total += i.value
#     print(int(round(total/num,0)))

#     # 중앙값
#     merge = Merge()
#     num_list = merge.merge_sort(num_list)
#     print(num_list[num//2])

#     # 최빈값
#     min_list: list[Number] = make_set(num_list)
#     min_list = merge.merge_sort_time(min_list)
#     min_value = min_list[0].time
#     temp_min: list[Number] = []
#     for i in min_list:
#         if min_value != i.time:
#             break
#         temp_min.append(i)
#     if len(temp_min) == 1:
#         print(temp_min[0])
#     else:
#         temp_min = merge.merge_sort(temp_min)
#         print(temp_min[1])

#     # 범위
#     print(num_list[-1].value - num_list[0].value)    
"""
Time Out..!! ^
"""
import sys
from collections import Counter

n = int(sys.stdin.readline())
a: int=[]
for i in range(n):
    a.append(int(sys.stdin.readline()))

#산술 평균
print(round(sum(a)/n))

# 중앙값
print(sorted(a)[len(a)//2])

# 최빈값
count = Counter(a) # 빈도수 구해주는 함수
order = count.most_common() # 수와 빈도수가 저장된 딕셔너리
max_freq = order[0][1]

freq: list[int] = []
for i in order:
    if i[1] == max_freq:
        freq.append(i[0])
if len(freq) == 1:
    print(freq[0])
else:
    print(sorted(freq)[1])

print(max(a)-min(a))