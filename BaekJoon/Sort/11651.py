import sys
import random

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x} {self.y}"

class Quick:
    def __init__(self):
        pass
    
    def __swap(self, temp: list[Position], n1: int, n2: int):
        temp[n1], temp[n2] = temp[n2], temp[n1]

    def __pivot(self, temp: list[Position], start: int, end: int):
        self.__swap(temp, start, random.randint(start, end))
        swap_point = start

        for i in range(start+1, end+1):
            if temp[i].y < temp[start].y:
                swap_point+=1
                self.__swap(temp, i, swap_point)
            elif temp[i].y == temp[start].y:
                if temp[i].x < temp[start].x:
                    swap_point += 1
                    self.__swap(temp, i , swap_point)
        self.__swap(temp, start, swap_point)

        return swap_point
    
    def __sort(self, temp: list[Position], start, end):
        if start < end:
            pivot_point = self.__pivot(temp, start, end)
            self.__sort(temp, start, pivot_point-1)
            self.__sort(temp, pivot_point+1, end)
        return temp
    
    def quick_sort(self, temp: list[Position]):
        return self.__sort(temp, 0, len(temp)-1)

if __name__=="__main__":
    num=int(sys.stdin.readline())
    quick = Quick()

    pos_list = []
    for _ in range(num):
        temp = tuple(map(int, sys.stdin.readline().strip().split()))
        pos_list.append(Position(temp[0],temp[1]))
    
    quick.quick_sort(pos_list)
    for p in pos_list:
        print(p)