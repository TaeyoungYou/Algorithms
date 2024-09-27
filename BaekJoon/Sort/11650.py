import sys
import random

class Position:
    def __init__(self, x:int, y:int):
        self.x=x
        self.y=y
    
    def __str__(self):
        return f"{self.x} {self.y}"

class Quick:
    def __init__(self):
        pass

    def __swap(self, temp: list[Position], i:int, j:int):
        temp[i], temp[j] = temp[j], temp[i]
    
    def __pivot(self, temp: list[Position], start: int, end: int):
        self.__swap(temp, start, random.randint(start, end))
        swap_index = start
        for i in range(start+1, end+1):
            if temp[i].x < temp[start].x:
                swap_index += 1
                self.__swap(temp, i, swap_index)
            elif temp[i].x == temp[start].x:
                if temp[i].y < temp[start].y:
                    swap_index += 1
                    self.__swap(temp, i, swap_index)
        self.__swap(temp, start, swap_index)
        return swap_index
    
    def __quick_sort(self, temp: list[Position], start: int, end: int):
        if start < end:
            pivot = self.__pivot(temp, start, end)
            self.__quick_sort(temp, start, pivot-1)
            self.__quick_sort(temp, pivot+1, end)
        return temp

    def sort(self, temp: list[Position]):
        return self.__quick_sort(temp, 0, len(temp)-1)

if __name__=="__main__":
    sort_driver = Quick()
    num=int(sys.stdin.readline())

    positions: list[Position] = []
    for _ in range(num):
        temp = tuple(map(int, sys.stdin.readline().strip().split()))
        positions.append(Position(temp[0], temp[1]))
    sort_driver.sort(positions)
    for p in positions:
        print(p)