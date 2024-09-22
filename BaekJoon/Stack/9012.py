import sys

class Node:
    def __init__(self, value:str):
        self.value=value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    def push(self, value: str) -> bool:
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
        else:
            if self.top.value == "(" and newNode.value == ")":
                self.pop()
                return True
            newNode.next = self.top
            self.top = newNode
        return True
    def pop(self) -> Node:
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp
    def getTop(self) -> Node:
        if self.top is None:
            return None
        return self.top
    def flush(self):
        while self.top is not None:
            self.top = self.top.next
    
if __name__=="__main__":
    stack=Stack()
    count=int(sys.stdin.readline())
    for _ in range(count):
        line=list(sys.stdin.readline().rstrip())
        for s in line:
            stack.push(s)
        if stack.getTop() is None:
            print("YES")
        else:
            print("NO")
        stack.flush()