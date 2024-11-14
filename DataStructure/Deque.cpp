#include<iostream>

using namespace std;

struct Node {
    int data;
    Node* prev;
    Node* next;

    explicit Node(int value) : data(value), prev(nullptr), next(nullptr){}
};

class Deque {
private:
    Node* head;
    Node* tail;
    int size;

public:
    explicit Deque() : head(nullptr), tail(nullptr), size(0){}

    // 앞에 요소 추가
    void push_front(int value) {
        Node* newNode = new Node(value);
        if(empty()) {
            head = tail = newNode;
        } else {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
        size++;
    }

    // 뒤에 요소 추가
    void push_back(int value) {
        Node* newNode = new Node(value);

        if(empty()){
            head = tail = newNode;
        } else {
            newNode->prev = tail;
            tail->next = newNode;
            tail = newNode;
        }
        size++;
    }

    // 앞 요소 제거
    void pop_front() {
        if(empty()) {
            return;
        }

        Node* temp = head;
        head = head->next;
        if(head != nullptr) {
            head->prev=nullptr;
        } else {
            tail = nullptr;
        }
        delete temp;
        size--;
    }

    // 뒤 요소 제거
    void pop_back() {
        if(empty()) {
            return;
        }

        Node* temp = tail;
        tail = tail->prev;
        if(tail != nullptr) {
            tail->next = nullptr;
        } else {
            head = nullptr;
        }
        delete temp;
        size--;
    }

    // 앞 요소 반환
    int front() const {
        if(empty()) {
            return -1;
        }
        return head->data;
    }

    // 뒤 요소 변경
    int back() const {
        if(empty()) {
            return -1;
        }
        return tail->data;
    }

    // 비어 있는지 확인
    bool empty() const {
        return size == 0;
    }

    // 크기 반환
    int getSize() const {
        return size;
    }

    ~Deque() {
        while(!empty()) {
            pop_front();
        }
    }
};

int main() {
    Deque deque;

    deque.push_back(10);
    deque.push_front(5);
    deque.push_back(15);

    cout<<"Front element: "<<deque.front()<<endl;
    cout<<"Back element: "<<deque.back()<<endl;

    deque.pop_front();
    cout<<"Front element after pop_front: "<<deque.front()<<endl;

    deque.pop_back();
    cout<<"Back element after pop_back: "<<deque.back()<<endl;

    cout<<"Size: "<<deque.getSize()<<endl;

    return EXIT_SUCCESS;
}