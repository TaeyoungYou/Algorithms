import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def push(self, value):
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1
    
    def pop(self):
        if self.top is None:
            return -1
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        return temp.value
    
    def get_top(self):
        if self.isEmpty():
            return ""
        return self.top.value
    
    def isEmpty(self):
        if self.top is None:
            return True
        return False
    
if __name__=="__main__":
    while True:
        line = list(sys.stdin.readline().rstrip())
        if line[0] == '.':
            break
        isYes = True
        stack=Stack()
        for c in line:
            if c in ['(','[']:
                stack.push(c)
            elif c == ')':
                if stack.get_top() == '(':
                    stack.pop()
                else:
                    isYes = False
                    break
            elif c == ']':
                if stack.get_top() == '[':
                    stack.pop()
                else:
                    isYes = False
                    break
        if isYes and stack.isEmpty():
            print("yes")
        else:
            print("no")