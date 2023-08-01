#include <iostream>
#include <string>

class Node {
private:
    int val;
    std::shared_ptr<Node> l;
    std::shared_ptr<Node> r;

public:
    Node(int a) : val{ a } {};
    Node(int a, std::shared_ptr<Node> const left, std::shared_ptr<Node> const right) : val{ a }, l{ left }, r{ right } {};

    ~Node() {};

    int value() const {
        return val;
    };

    std::shared_ptr<Node> left() const {
        return std::shared_ptr<Node>{l};
    }

    std::shared_ptr<Node> right() const {
        return std::shared_ptr<Node>{r};
    }

    std::shared_ptr<Node> addNode(int v) {
        if (v > val) {
            if (r != nullptr) {
                return (r->addNode(v));
            }
            else {
                r = std::shared_ptr<Node>{ new Node(v) };
                return r;
            }
        }
        if (v < val) {
            if (l != nullptr) {
                return (l->addNode(v));
            }
            else {
                l = std::shared_ptr<Node>{ new Node(v) };
                return l;
            }
        }
    };

    //TODO
    std::shared_ptr<Node> removeNode(int v) {
        if (v > val) {
            if (r != nullptr) {
                return (r->removeNode(v));
            }
            else {


            }
        }
        if (v < val) {
            if (l != nullptr) {
                return (l->removeNode(v));
            }
            else {


            }
        }
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

};

std::ostream& operator<<(std::ostream& os, const Node& n) {
    return os << "{" << n.value() << ", " << n.left() << ", " << n.right() << "}" << std::endl;
};

int main() {
    std::shared_ptr<Node> n {new Node(5)};
    std::shared_ptr<Node> l = n->addNode(4);
    std::shared_ptr<Node> r = n->addNode(6);
    std::cout << n->nlr() << std::endl << n->lrn() << std::endl << n->lnr();
}