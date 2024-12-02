#include<iostream>
#include<vector>
using namespace std;

class MaxHeap {
private:
    vector<int> heap;

    void heapifyUp(int index) {
        int parent = (index - 1) / 2;
        while(index > 0 && heap[index] > heap[parent]) {
            swap(heap[index] , heap[parent]);
            index = parent;
            parent = (index - 1) / 2;
        }
    }

    void heapifyDown(int index) {
        int size = heap.size();
        int large = index;
        int left = (index * 2) + 1;
        int right = (index * 2) + 2;

        if(left < size && heap[left] > heap[large]) {
            large = left;
        }
        if(right < size && heap[right] > heap[large]) {
            large = right;
        }
        if(large != index) {
            swap(heap[index], heap[large]);
            heapifyDown(large);
        }
    }

public:
    void insert(int value) {
        heap.push_back(value);
        heapifyUp(heap.size() - 1);
    }

    int deleteMax() {
        if(heap.empty()) {
            throw runtime_error("Heap is empty");
        }
        int maxVal = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        if(!heap.empty()) {
            heapifyDown(0);
        }
        return maxVal;
    }

    int peek() const {
        if(heap.empty()) {
            throw runtime_error("Heap is empty");
        }
        return heap[0];
    }

    void printHeap() const {
        for(int val : heap) {
            cout<<val<<" ";
        }
        cout<<endl;
    }
};

int main() {
    MaxHeap maxheap;

    maxheap.insert(10);
    maxheap.insert(50);
    maxheap.insert(40);
    maxheap.insert(60);
    maxheap.insert(1);

    cout<<"Heap Elements:"<<endl;
    maxheap.printHeap();

    cout<<"Max element: "<<maxheap.peek()<<endl;
    maxheap.deleteMax();
    cout<<"After Deletion"<<endl;
    maxheap.printHeap();

    return EXIT_SUCCESS;
}