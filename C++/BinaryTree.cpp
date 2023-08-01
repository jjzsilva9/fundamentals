#include <iostream>
#include <ostream>

class Node {
    private:
        int val;
        //std::unique_ptr<Node> left = nullptr;
        Node* left = nullptr;
        //std::unique_ptr<Node> right = nullptr;
        Node* right = nullptr;

    public:
        Node(int a) : val{a} {};
        Node(int a, Node& const l, Node& const r) : val{a}, left{&l}, right{&r} {};

        ostream& operator<<(ostream& os, const Node& n) {
            return os << "{" << val << ", " << left << ", " << right << std::endl;
        };

};

int main() {
    Node r(6);
    Node l(4);
    Node n(5, l, r);
    return 0;
}