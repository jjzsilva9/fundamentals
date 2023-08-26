#include <iostream>
#include <string>
#include <stdexcept>

class Node {
private:
    int val;
    Node* l = nullptr;
    Node* r = nullptr;

public:
    Node(int a) : val{ a } {};
    Node(int a, Node* const left, Node* const right) : val{ a }, l{ left }, r{ right } {};

    ~Node() {};

    int value() const {
        return val;
    };

    Node* left() const {
        return l;
    }

    Node* right() const {
        return r;
    }

    int addNode(int v) {
        if (v > val) {
            if (r != nullptr) {
                r->addNode(v);
                return 0;
            }
            else {
                r = { new Node(v) };
                return 0;
            }
        }
        if (v < val) {
            if (l != nullptr) {
                l->addNode(v);
                return 0;
            }
            else {
                l = { new Node(v) };
                return 0;
            }
        }
        return 1;
    };

    void setValue(int v) {
        val = v;
    }

    Node* findNode(int v) {
        if (v == val) {
            return this;
        }
        else if (v > val) {
            if (r != nullptr) {
                return r->findNode(v);
            }
            else {
                return nullptr;
            }
        }
        else if (v < val) {
            if (l != nullptr) {
                return l->findNode(v);
            }
            else {
                return nullptr;
            }
        }
    }

    //TODO
    Node* removeNode(int v) {
        Node* p = findParent(v);
        Node* c = nullptr;
        if (p == nullptr) {
            c = findNode(v);
        }
        else {
            if (p->left() != nullptr) {
                if (p->left()->value() == v) {
                    c = p->left();
                }
                else {
                    c = p->right();
                }
            }
            else {
                c = p->right();
            }
        }
       
        if (c == nullptr) {
            return this;
        }
        if (c->left() != nullptr && c->right() != nullptr) {
            Node* leftmostParent = r->findLeftmostParent();
            if (leftmostParent->left()->right() != nullptr) {
                int temp = c->value();
                c->setValue(leftmostParent->left()->value());
                leftmostParent->left()->setValue(temp);
                Node* ans = leftmostParent->left();
                leftmostParent->setLeft(leftmostParent->left()->right());
                return ans;
            }
        }
        else if (c->left() != nullptr){
            if (p == nullptr) {
                return c->left();
            }
            else if (p->left() != nullptr && p->left() == c) {
                p->setLeft(c->left());
                return this;
            }
            else if (p->right() != nullptr && p->right() == c) {
                p->setRight(c->left());
                return this;
            }
        }
        else if (c->right() != nullptr) {
            if (p == nullptr) {
                return c->right();
            }
            else if (p->left() != nullptr && p->left() == c) {
                p->setLeft(c->right());
                return this;
            }
            else if (p->right() != nullptr && p->right() == c) {
                p->setRight(c->right());
                return this;
            }
        }
        else {
            if (p == nullptr) {
                return nullptr;
            }
            else if (p->left() == c) {
                p->setLeft(nullptr);
                return this;
            }
            else if (p->right() == c) {
                p->setRight(nullptr);
                return this;
            }
        }
        
    }

    void setLeft(Node* v) {
        l = v;
    }

    void setRight(Node* v) {
        r = v;
    }

    Node* findLeftmost() {
        if (l != nullptr) {
            return l->findLeftmost();
        }
        else {
            return this;
        }
    }

    Node* findLeftmostParent() {
        if (l->left() != nullptr) {
            return l->findLeftmost();
        }
        else {
            return this;
        }
    }

    Node* findRightmost() {
        if (r->right() != nullptr) {
            return r->findLeftmost();
        }
        else {
            return this;
        }
    }

    Node* findRightmostParent() {
        if (r != nullptr) {
            return r->findLeftmost();
        }
        else {
            return this;
        }
    }

    Node* findParent(int v) {
        if (v > val) {
            if (r != nullptr) {
                if (r->value() == v) {
                    return this;
                }
                return r->findParent(v);
            }
            else {
                return nullptr;
            }
        }
        else if (v < val) {
            if (l != nullptr) {
                if (l->value() == v) {
                    return this;
                }
                return l->findParent(v);
            }
            else {
                return nullptr;
            }
        }
        return nullptr;
    }

    std::string nlr() const {
        std::string ans = "";
        ans += std::to_string(val);
        ans += "\n";
        if (l != nullptr) {
            ans += (l->nlr());
        }
        if (r != nullptr) {
            ans += (r->nlr());
        }
        return ans;
    }

    std::string lnr() const {
        std::string ans = "";
        if (l != nullptr) {
            ans += (l->nlr());
        }
        ans += std::to_string(val);
        ans += "\n";
        if (r != nullptr) {
            ans += (r->nlr());
        }
        return ans;
    }

    std::string lrn() const {
        std::string ans = "";
        if (l != nullptr) {
            ans += (l->nlr());
        }
        if (r != nullptr) {
            ans += (r->nlr());
        }
        ans += std::to_string(val);
        ans += "\n";
        return ans;
    }

    void swapNodes(Node* a, Node* b) {
        if (a == nullptr) {
            if (b != nullptr) {
                a = new Node(b->value(), b->left(), b->right());
                b = nullptr;
                return;
            }
            else {
                return;
            }
        }
        else if (b == nullptr) {
            if (a != nullptr) {
                b = new Node(a->value(), a->left(), a->right());
                a = nullptr;
                return;
            }
            else {
                return;
            }
        }
        int tempVal = a->value();
        Node* tempLeft = a->left();
        Node* tempRight = a->right();
        a->setValue(b->value());
        a->setLeft(b->left());
        a->setRight(b->right());
        b->setValue(tempVal);
        b->setLeft(tempLeft);
        b->setRight(tempRight);
    }

    void rotateLeft() {
        if (r != nullptr) {
            Node* const root = r;
            Node* const rootLeft = root->left();

            setRight(rootLeft);

            root->setLeft(this);
            swapNodes(this, root);
        }

    }

    void rotateRight() {
        if (l != nullptr) {
            Node* const root = l;
            Node* const rootRight = root->right();

            setRight(rootRight);

            root->setRight(this);
            swapNodes(this, root);
        }
    }

};

std::ostream& operator<<(std::ostream& os, const Node& n) {
    os << "{" << n.value() << ", ";
    if (n.left() != nullptr) {
        os << "Left: " << n.left()->value();
    }
    else {
        os << "Left: Null";
    }
    if (n.right() != nullptr) {
        os << ", Right: " << n.right()->value();
    }
    else {
        os << ", Right: Null";
    }
    return os << "}" << std::endl;//<< "{" << n.value() << ", " << n.left() << ", " << n.right() << "}" << std::endl;
};

int main() {
    Node n = Node(3);
    n.addNode(4);
    n.addNode(6);
    n.addNode(5);

    std::cout << n.nlr();
    n.rotateLeft();
    std::cout << n;
    std::cout << n.nlr();
}