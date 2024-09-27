import sys

class Account:
    def __init__(self, serial_num: int, age: int, name: str):
        self. serial_number = serial_num
        self.age = age
        self.name = name
    
    def toString(self):
        return f"{self.age} {self.name}"

class Quick:
    def __init__(self):
        pass
    
    def swap(self, temp: list[Account], i: int, j: int):
        temp[i], temp[j] = temp[j], temp[i]

    def _pivot(self, temp: list[Account], pivot: int, end: int):
        swap_index = pivot
        for i in range(pivot+1, end+1):
            if temp[i].age < temp[pivot].age:
                swap_index += 1
                self.swap(temp, swap_index, i)
            elif temp[i].age == temp[pivot].age:
                if temp[i].serial_number < temp[pivot].serial_number:
                    swap_index += 1
                    self.swap(temp, swap_index, i)
        self.swap(temp, pivot, swap_index)
        return swap_index
    
    def _quick_sort(self, temp: list[Account], start: int, end: int):
        if start < end:
            pivot = self._pivot(temp, start, end)
            self._quick_sort(temp, start, pivot-1)
            self._quick_sort(temp, pivot+1, end)
        return temp
    
    def sort(self, temp: list[Account]):
        return self._quick_sort(temp, 0, len(temp)-1)


if __name__=="__main__":
    driver = Quick()

    num=int(sys.stdin.readline())
    accounts: list[Account] = []
    for i in range(num):
        temp = tuple(sys.stdin.readline().rstrip().split())
        accounts.append(Account(i, int(temp[0]),temp[1]))
    
    driver.sort(accounts)
    for a in accounts:
        print(a.toString())