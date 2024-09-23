import sys

class Node:
    def __init__(self, value):
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
    
    def size(self) -> int:
        return self.length
    
    def empty(self) -> int:
        if self.front is None:
            return 1
        return 0
    
    def get_front(self) -> int:
        if self.empty():
            return -1
        return self.front.value
    
    def get_back(self) -> int:
        if self.empty():
            return -1
        return self.back.value
    
if __name__ == "__main__":
    operate_length = int(sys.stdin.readline())

    queue = Queue()
    for _ in range(operate_length):
        operation = list(sys.stdin.readline().strip().split())

        if operation[0] == "push":
            queue.push(int(operation[1]))
        elif operation[0] == "pop":
            print(queue.pop())
        elif operation[0] == "size":
            print(queue.size())
        elif operation[0] == "empty":
            print(queue.empty())
        elif operation[0] == "front":
            print(queue.get_front())
        elif operation[0] == "back":
            print(queue.get_back())