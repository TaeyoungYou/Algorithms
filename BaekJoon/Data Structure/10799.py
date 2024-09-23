"""
Razer: ()
Stick: ( )

레이저로 자르고 스택에서 나갈 때, 전에 남아있는 스택 갯수를 반환
레이저가 아닌 것은 1를 반환
"""
import sys

class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        self.isRazer=True

class Stack:
    def __init__(self):
        self.top=None
        self.depth=0
    def push(self, value):
        newNode=Node(value)
        if self.top is None:
            self.top = newNode
        else:
            self.top.isRazer = False
            newNode.next = self.top
            self.top = newNode
        self.depth += 1
    
    def pop(self):
        if self.top is None:
            return  None
        temp=self.top
        self.top=self.top.next
        temp.next=None
        self.depth -= 1
        return temp
    def getTop(self):
        if self.top is None:
            return None
        return self.top
    def getSize(self):
        return self.depth

if __name__ == "__main__":
    operation=list(sys.stdin.readline().rstrip())
    stack=Stack()
    total = 0
    for s in operation:
        if stack.getTop() is None:
            stack.push(s)
        elif stack.getTop().value == "(" and s == ")":
            if stack.getTop().isRazer:
                stack.pop()
                total += stack.getSize()    
            else:
                stack.pop()
                total += 1
        else:
            stack.push(s)
    print(total)