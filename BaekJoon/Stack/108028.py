import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value: int) -> None:
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        return True

    def pop(self) -> int:
        if self.top is None:
            return -1
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value
    
    def size(self) -> int:
        curPos = self.top
        size = 0
        while curPos is not None:
            curPos = curPos.next
            size += 1
        return size
    
    def empty(self) -> int:
        if self.top is None:
            return 1
        return 0
    
    def getTop(self) -> int:
        if self.top is None:
            return -1
        return self.top.value

if __name__ == "__main__":
    count=int(sys.stdin.readline())
    stack = Stack()
    for _ in range(count):
        operation=list(sys.stdin.readline().rstrip().split())

        if operation[0] == "push":
            stack.push(int(operation[1]))
        elif operation[0] == "pop":
            print(stack.pop())
        elif operation[0] == "size":
            print(stack.size())
        elif operation[0] == "empty":
            print(stack.empty())
        elif operation[0] == "top":
            print(stack.getTop())