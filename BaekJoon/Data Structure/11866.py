import sys

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0
    
    def push(self, value: int) -> None:
        newNode = Node(value)
        if self.front is None:
            self.front = newNode
            self.back = newNode
        else:
            self.back.next = newNode
            self.back = newNode
        self.length += 1
    
    def pop(self) -> int:
        if self.front is None:
            return -1
        temp = self.front
        if self.length == 1:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next
            temp.next = None
        self.length -= 1
        return temp.value
    
    def empty(self) -> bool:
        if self.front is None:
            return True
        return False

if __name__ == "__main__":
    recur_max, time = map(int, sys.stdin.readline().split())

    queue = Queue()

    source = list(n for n in range(1,recur_max+1))
    i = 0
    while source != []:
        temp = i + time - 1 
        while len(source)-1 < temp:
            temp = temp - len(source)
        queue.push(source.pop(temp))
        i = temp
    temp = []
    while not queue.empty():
        temp.append(queue.pop())
    print("<"+", ".join(map(str,temp))+">")

"""
요세푸스 문제는 원형 링크드 리스트로도 구현가능하고 더 효율적임
"""