import sys

class Number:
    def __init__(self, value):
        self.value = value
        self.time = 1

class Merge:
    def __init__(self):
        pass
    
    def __merge(self, temp1: list[Number], temp2: list[Number]):
        i,j = 0,0
        res_list = []
        while i<len(temp1) and j<len(temp2):
            if temp1[i].value < temp2[j].value:
                res_list.append(temp1[i])
                i+=1
            else:
                res_list.append(temp2[j])
                j+=1
        
        while i<len(temp1):
            res_list.append(temp1[i])
            i+=1
        while j<len(temp2):
            res_list.append(temp2[j])
            j+=1
        return res_list
    
    def merge_sort(self, temp: list[Number]):
        if len(temp) < 1:
            return temp
        mid_pos = len(temp)//2
        left = self.merge__sort(temp[:mid_pos])
        right = self.merge_sort(temp[mid_pos:])

        return self.__merge(left, right)

def make_set(temp: list[Number]):
    

if __name__=="__main__":
    num = int(sys.stdin.readline())
    num_list = []
    for _ in range(num):
        num_list.append(Number(int(sys.stdin.readline())))