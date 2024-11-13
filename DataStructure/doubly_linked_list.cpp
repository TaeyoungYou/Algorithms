/**
 * Doubly Linked List
 * 각 노드가 이전 노드와 다음 노드를 가리키는 포인터 두개를 가짐
 * 양방향으로 탐색이 가능한 리스트
 */

#include<iostream>
#include<string>

using namespace std;

struct Node {
    int data; // 데이터를 저장할 멤버 변수
    Node *prev; // 이전 노드를 가리키는 포인터
    Node *next; // 다음 노드를 가리키는 포인터

    explicit Node(int data) : data(data), prev(nullptr), next(nullptr) {
    } // 생성자를 통해 초기화
};

class DoublyLinkedList {
private:
    Node *head; // 리스트의 첫번째 노드를 가리키는 포인터
    Node *tail; // 리스트의 마지막 노드를 가리키는 포인터

public:
    DoublyLinkedList() : head(nullptr), tail(nullptr) {
    } // 초기화

    // 1. 리스트의 끝에 노드 추가 (append)
    void append(int data) {
        Node *newNode = new Node(data);
        if (tail == nullptr) {  // 리스트가 비어 있는 경우
            head = tail = newNode;
        } else {    // 리스트가 비어있지 않는 경우
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }

    // 2. 리스트의 맨 앞에 노드 추가 (prepend)
    void prepend(int data) {
        Node *newNode = new Node(data);
        if (head == nullptr) {  // 리스트가 비어있는 경우
            head = tail = newNode;
        } else {    // 리스트가 비어있지 않는 경우
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
    }

    // 3. 리스트에서 특정 데이터를 가진 노드 삭제
    void deleteNode(int key) {
        Node *cur = head;

        while (cur != nullptr && cur->data != key) {
            cur = cur->next;
        }

        if (cur == nullptr) return; // 노드를 찾지 못한 경우

        if (cur == head) {  // 삭제할 노드가 head인 경우
            head = cur->next;
            if (head) head->prev = nullptr;
        } else if (cur == tail) {   // 삭제할 노드가 tail인 경우
            tail = cur->prev;
            if (tail) tail->next = nullptr;
        } else {    // 중간 노드 삭제
            cur->prev->next = cur->next;
            cur->next->prev = cur->prev;
        }
        delete cur; // 메모리 해제
    }

    // 4. 리스트 출력 (앞에서 뒤로)
    void displayForward() const {
        Node* temp = head;
        cout<<"nullptr <-> ";
        while(temp != nullptr) {
            cout<<temp->data<<" <-> ";
            temp = temp->next;
        }
        cout<<"nullptr"<<endl;
    }

    // 5. 리스트 출력 (뒤에서 앞으로)
    void displayBackward() const {
        Node* temp = tail;
        cout<<"nullptr <-> ";
        while(temp != nullptr) {
            cout<<temp->data<<" <-> ";
            temp = temp->prev;
        }
        cout<<"nullptr"<<endl;
    }
};

int main() {
    DoublyLinkedList list;

    // 노드 추가
    list.append(10);
    list.append(20);
    list.prepend(5);

    // 리스트 출력
    cout<<"Forward Display: "<<endl;
    list.displayForward();

    cout<<"Backward Display: "<<endl;
    list.displayBackward();

    // 노드 삭제
    list.deleteNode(20);
    cout<<"After deletion 20 (Forward)"<<endl;
    list.displayForward();

    return EXIT_SUCCESS;
}
