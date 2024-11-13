#include<iostream>

using namespace std;

struct Node {
    int data;
    Node* next;

    explicit Node(int value) : data(value), next(nullptr){}
};

class Stack {
private:
    Node* topNode;

public:
    explicit Stack() : topNode(nullptr){}

    // 스택에 요소 추가
    void push(int value) {
        Node* newNode = new Node(value);
        newNode->next = topNode;
        topNode = newNode;
    }

    // 스택의 맨 위 요소 제거
    void pop() {
        // 스택이 비어있는 지
        if(empty()) return;

        Node* temp = topNode;
        topNode = topNode->next;
        delete temp;
    }

    // 스택의 맨 위 요소 반환
    int top() const {
        if(empty()) return -1;
        return topNode->data;
    }

    // 스택이 비어있는지 확인
    bool empty() const {
        return topNode == nullptr;
    }

    // 스택의 크기 반환
    int size() const {
        int count = 0;
        Node* cur = topNode;
        while(cur != nullptr) {
            count++;
            cur = cur->next;
        }
        return count;
    }

    ~Stack() {
        while(!empty()) {
            pop();
        }
    }
};

int main() {
    Stack stack;

    stack.push(10);
    stack.push(20);
    stack.push(30);

    cout<<"Top element: "<<stack.top()<<endl;
    stack.pop();
    cout<<"Top element: "<<stack.top()<<endl;
    cout<<"Stack size: "<<stack.size()<<endl;

    if(stack.empty()) {
        cout<<"Stack is empty"<<endl;
    }else {
        cout<<"Stack is not empty"<<endl;
    }

    return EXIT_SUCCESS;
}