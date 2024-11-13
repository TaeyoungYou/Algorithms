/**
 * Singly Linked List
 * 각 노드가 다음 노드를 가리키는 포인터를 포함하여 구성된 자료구조
 */

#include<iostream>
#include<string>
using namespace std;

struct Node {
    int data;   // int 데이터 저장
    Node* next; // 다음 노드를 가리키는 포인터

    explicit Node(int value) : data(value), next(nullptr) {}    // 생성자를 통해 데이터 초기화
};

class SinglyLinkedList {
private:
    Node* head;     // 리스트의 첫 번째 노드를 가리키는 포인터

public:
    SinglyLinkedList() : head(nullptr){}    // 초기에는 head가 nullptr

    // 1. 리스트에 맨 앞에 새 노드를 추가
    void insertAtHead(int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
    }

    // 2. 리스트의 맨 끝에 새 노드를 추가
    void insertAtTail(int data) {
        Node* newNode = new Node(data);
        if(head == nullptr) {
            head = newNode;
        }else {
            Node* temp = head;
            while(temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
    }

    // 3. 리스트에서 특정 데이터를 가진 노드를 삭제
    void deleteNode(int key) {
        if(head == nullptr) return;

        if(head->data == key) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }

        Node* cur = head;
        while(cur->next != nullptr && cur->next->data != key) {
            cur = cur->next;
        }
        if(cur->next == nullptr) return;

        Node* temp = cur->next;
        cur->next  =cur->next->next;
        delete temp;
    }

    // 4. 리스트를 출력
    void display() const {
        Node* temp = head;
        while(temp != nullptr) {
            cout<<temp->data<<" -> ";
            temp = temp->next;
        }
        cout<<"nullptr"<<endl;
    }
};

int main() {
    SinglyLinkedList list;

    list.insertAtHead(10);
    list.insertAtHead(20);
    list.insertAtHead(30);
    list.insertAtHead(40);

    cout<<"Initail List: "<<endl;
    list.display();

    list.deleteNode(20);
    cout<<"After deleting 20: "<<endl;
    list.display();

    list.deleteNode(40);
    cout<<"After deleting 40: "<<endl;
    list.display();

    return EXIT_SUCCESS;
}