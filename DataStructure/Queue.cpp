#include <deque>
#include<iostream>

using namespace std;

struct Node {
    int data;
    Node* next;

    explicit Node(int value) : data(value), next(nullptr){}
};

class Queue {
private:
    Node* frontNode;
    Node* rearNode;
    int size;

public:
    explicit Queue() : frontNode(nullptr), rearNode(nullptr), size(0){}

    // 큐에 요소 추가
    void enqueue(int value) {
        Node* newNode = new Node(value);
        if(empty()) {
            frontNode = rearNode = newNode;
        } else {
            rearNode->next = newNode;
            rearNode = newNode;
        }
        size++;
    }

    // 큐의 앞에서 요소 제거
    void dequeue() {
        if(empty()) {
            return;
        }
        Node* temp = frontNode;
        frontNode = frontNode->next;
        delete temp;
        size--;
        if(frontNode == nullptr) {
            rearNode = nullptr;
        }
    }

    // 큐의 앞 요소 반환
    int front() const {
        if(empty()) {
            return -1;
        }
        return frontNode->data;
    }

    // 큐가 비어있는지 확인
    bool empty() const {
        return frontNode == nullptr;
    }

    // 큐의 크기 반환
    int getSize() const {
        return size;
    }

    ~Queue() {
        while(!empty()) {
            dequeue();
        }
    }
};

int main() {
    Queue queue;

    queue.enqueue(10);
    queue.enqueue(20);
    queue.enqueue(30);

    cout<<"Front element: "<<queue.front()<<endl;
    queue.dequeue();
    cout<<"Front element: "<<queue.front()<<endl;
    cout<<"Queue size: "<<queue.getSize()<<endl;

    if(queue.empty()) {
        cout<<"Queue is empty"<<endl;
    }else {
        cout<<"Queue is not empty"<<endl;
    }

    return EXIT_SUCCESS;
}