import sys


# def _merge(list1, list2):
#     temp = []
#     i,j=0,0
#     while len(list1) > i and len(list2) > j:
#         if list1[i] < list2[j]:
#             temp.append(list1[i])
#             i+=1
#         else:
#             temp.append(list2[j])
#             j+=1

#     while len(list1) > i:
#         temp.append(list1[i])
#         i+=1
    
#     while len(list2) > j:
#         temp.append(list2[j])
#         j+=1
#     return temp

# def merge_sort(list1):
#     if len(list1) <= 1:
#         return list1

#     mid = len(list1)//2

#     left=merge_sort(list1[:mid])
#     right=merge_sort(list1[mid:])

#     return _merge(left,right)

# if __name__=="__main__":
#     total=int(sys.stdin.readline())

#     num_list = []
#     for _ in range(total):
#         num_list.append(int(sys.stdin.readline()))
#     num_list = merge_sort(num_list)
#     for n in num_list:
#         print(n)
"""
메모리 초과로 인한 실패
정렬하지 않고, output은 정렬하게
"""

temp=[0]*10001
num=int(sys.stdin.readline())
for _ in range(num):
    temp[int(sys.stdin.readline())] += 1
for i,v in enumerate(temp):
    if v != 0:
        for _ in range(v):
            print(i)