#include <iostream>

class Node {
    private:
        int val = NULL;
        Node* left = nullptr;
        Node* right = nullptr;

    public:
        Node(int a) : val{a} {}

};

int main() {
    Node n(5);
    return 0;
}