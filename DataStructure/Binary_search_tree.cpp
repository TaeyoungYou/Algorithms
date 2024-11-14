#include<iostream>
using namespace std;

struct Node {
    int  data;
    Node* left;
    Node* right;

    explicit Node(int value) : data(value), left(nullptr), right(nullptr){}
};

class BinarySearchTree {
private:
    Node* root;

    // 삽입 함수 (재귀)
    Node* insert(Node* node, int value) {
        if(node == nullptr) {
            return new Node(value);
        }
        if(value < node->data) {
            node->left = insert(node->left, value);
        } else if(value > node->data) {
            node->right = insert(node->right, value);
        }
        return node;
    }

    // 탐색 함수 (재귀)
    bool search(Node* node, int value) {
        if(node == nullptr) return false;
        if(node->data == value) return true;
        if(value < node->data) return search(node->left, value);
        return search(node->right, value);
    }

    // 삭제 함수 (재귀)
    Node* deleteNode(Node* node, int value) {
        if(node == nullptr) return nullptr;

        // 삭제할 값이 현재 노드의 값보다 작으면 왼쪽 서브트리에서 탐색
        if(value < node->data) {
            node->left = deleteNode(node->left, value);
        } else if(value > node->data) {     // 삭제할 값이 현재 노드의 값보다 크면 오르쪽 서브트리에서 탐색
            node->right = deleteNode(node->right, value);
        } else {
            // 자식이 없는 경우
            if(node->left == nullptr && node->right == nullptr) {
                delete node;
                return nullptr;
            } else if(node->left == nullptr) {  // 자식이 하나: 오른쪽 자식이 있는 경우
                Node* temp = node->right;
                delete node;
                return temp;
            } else if(node->right == nullptr) { // 자식이 하나: 왼쪽 자식이 있는 경우
                Node* temp = node->left;
                delete node;
                return temp;
            } else {    // 자식이 둘인 경우
                // 오른쪽 자식에서 가장 작은 노드 찾기
                Node* temp = findMin(node->right);
                // 그 찾은 노드의 값을 넣기
                node->data = temp->data;
                // 오른쪽 자식에서 그 찾은 노드를 삭제
                node->right  = deleteNode(node->right, temp->data);
            }
        }
        return node;
    }

    // 최솟값 찾기 (삭제 연산에서 사용)
    Node* findMin(Node* node) {
        while(node->left != nullptr) {
            node = node->left;
        }
        return node;
    }

    // In-order Traversal
    void inorderTraversal(Node* node) {
        if(node == nullptr) return;
        inorderTraversal(node->left);
        cout<<node->data<<" ";
        inorderTraversal(node->right);
    }
public:
    // 생성자
    BinarySearchTree() : root(nullptr){}

    // 삽입 함수
    void insert(int value) {
        root = insert(root, value);
    }

    // 탐색 함수
    bool search(int value) {
        return search(root, value);
    }

    // 삭제 함수
    void deleteNode(int value) {
        root = deleteNode(root, value);
    }

    // Inorder 출력
    void inorderTraversal() {
        inorderTraversal(root);
        cout<<endl;
    }
};

int main() {
    BinarySearchTree bst;

    bst.insert(10);
    bst.insert(5);
    bst.insert(20);
    bst.insert(3);
    bst.insert(7);

    cout<<"In-order Traversal: "<<endl;
    bst.inorderTraversal();

    cout<<"Search for 10: "<<bst.search(10)<<endl;
    cout<<"Sear for 15: "<<bst.search(15)<<endl;

    bst.deleteNode(5);
    bst.inorderTraversal();

    return EXIT_SUCCESS;
}