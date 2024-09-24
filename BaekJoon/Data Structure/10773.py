import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def push(self, value: int) -> None:
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1

    def pop(self) -> int:
        if self.top is None:
            return -1
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        return temp.value
    
    def isEmpty(self) -> bool:
        if self.top is None:
            return True
        return False

if __name__ == "__main__":
    operation_time = int(sys.stdin.readline())

    stack = Stack()

    for _ in range(operation_time):
        num = int(sys.stdin.readline())
        if num == 0:
            stack.pop()
        else:
            stack.push(num)
    
    total = 0
    while not stack.isEmpty():
        total += stack.pop()
    print(total)