import sys

def _merge(list1, list2):
    merged = []
    i=0
    j=0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i+=1
        else:
            merged.append(list2[j])
            j+=1
    while i < len(list1):
        merged.append(list1[i])
        i+=1
    while j < len(list2):
        merged.append(list2[j])
        j+=1
    return merged

def merge_sort(list1):
    if len(list1) <= 1:
        return list1
    mid=len(list1)//2
    left = merge_sort(list1[:mid])
    right = merge_sort(list1[mid:])

    return _merge(left, right)

if __name__=="__main__":
    size=int(sys.stdin.readline())
    temp=[]
    for _ in range(size):
        temp.append(int(sys.stdin.readline()))
    temp = merge_sort(temp)
    for i in temp:
        print(i)