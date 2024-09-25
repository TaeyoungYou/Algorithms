import sys

class Merge_Sort:
    def __init__(self):
        pass

    def _merge(self, list1, list2):
        merged=[]
        i,j=0,0
        while i<len(list1) and j<len(list2):
            if len(list1[i]) < len(list2[j]):
                merged.append(list1[i])
                i+=1
            elif len(list2[j]) < len(list1[i]):
                merged.append(list2[j])
                j+=1
            else:
                if list1[i] == list2[j]:
                    merged.append(list1[i])
                    i+=1
                    j+=1
                    continue
                temp1=list1[i].split()
                temp2=list2[j].split()
                for k in range(len(list1[i])):
                    if temp1[k] < temp2[k]:
                        merged.append(list1[i])
                        i+=1
                        break
                    elif temp2[k] < temp1[k]:
                        merged.append(list2[j])
                        j+=1
                        break
        
        while i<len(list1):
            merged.append(list1[i])
            i+=1
        
        while j<len(list2):
            merged.append(list2[j])
            j+=1
        
        return merged
                    
    
    def merge_sort(self, list1):
        if len(list1) <= 1:
            return list1
        mid=len(list1)//2
        left=self.merge_sort(list1[:mid])
        right=self.merge_sort(list1[mid:])

        return self._merge(left, right)
        

if __name__=='__main__':
    size=int(sys.stdin.readline())
    word_list=[]
    for _ in range(size):
        word_list.append(sys.stdin.readline().strip())
    sort = Merge_Sort()
    word_list = sort.merge_sort(word_list)
    for w in word_list:
        print(w)