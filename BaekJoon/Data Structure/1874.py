"""
알고리즘:
1. stack의 top을 확인 후, 다음 수열과 같으면 pop
2. 계속해서 push
3. 1과 2가 아니면 NO

구현을 못함
"""
import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
    
    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp
    
    def see_top(self):
        return self.top

if __name__=="__main__":
    size = int(sys.stdin.readline())
    final_list = [0]*size
    for i in range(size):
        final_list[i] = int(sys.stdin.readline())
    stack = Stack()
    operations = []
    current = 1
    Works = True

    for num in final_list:
        while current <= num:
            stack.push(current)
            operations.append("+")
            current += 1
        
        if stack.see_top().value == num:
            stack.pop()
            operations.append("-")
        else:
            print("NO")
            Works = False
            break
    if Works:
        print("\n".join(operations))

