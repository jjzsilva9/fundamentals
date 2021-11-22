class stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.s = []

    def push(self, item):
        if len(self.s) == self.maxSize:
            print("Stack Overflow")
        else:
            self.s.append(item)
        print(self.s)

    def pop(self):
        if len(self.s) == 0:
            print("Stack Underflow")
        else:
            self.s.pop()
        print(self.s)

    def isEmpty(self):
        if len(self.s) == 0:
            return True
        else:
            return False

    def top(self):
        return self.s[0]

    def length(self):
        return len(self.s)

s1 = stack(5)
s1.push("Joe")
s1.pop()
s1.push("Ed")
s1.push("Seth")
s1.push("Elaine")
s1.push("Lucy")
s1.push("Ben")
print(s1.top())
print(s1.length())
print(s1.isEmpty())
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.pop()

