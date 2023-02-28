
class HashTable:
    def __init__(self, maxsize, keyType):
        self.maxsize = maxsize
        self.table = [""]*self.maxsize
        self.keyType = keyType

    def key(self, item):
        if self.keyType == "mod":
            index = item % self.maxsize
            return index
        if self.keyType == "midSquare":
            index = (item*item)
            if len(str(index)) > self.maxsize:
                index = str(index)[1:-1]
            index = index % self.maxsize
            print(index)
            return index
        if self.keyType == "folding":
            sum = 0
            for i in range(len(str(item))):
                sum = sum + int(str(item)[i])
            return sum%self.maxsize
        
    def add(self, item):
        if type(item) == int:
            print("Item is a number")
            index = self.key(item)
        elif type(item) == str:
            print("Item is a string")
            for char in item:
                if item.index(char) == 0:
                    index = ord(char)
                index += ord(char)
                print(index)
                index = self.key(index)
        written = False
        while written == False:
            if index == self.maxsize:
                index = 0
            if self.table[index] == "" or self.table[index] == "Deleted":
                self.table[index] = item
                written = True
                print(self.table)
            else:
                index += 1

    def remove(self, item):
        if type(item) == int:
            print("Item is a number")
            index = self.key(item)
        elif type(item) == str:
            print("Item is a string")
            for char in item:
                if item.index(char) == 0:
                    index = ord(char)
                index += ord(char)
                print(index)
                index = self.key(index)
        deleted = False
        while deleted == False:
            if index == self.maxsize:
                index = 0
            if self.table[index] == item:
                self.table[index] = "Deleted"
                deleted = True
                print(self.table)
            else:
                index += 1

    def search(self, item):
        if type(item) == int:
            print("Item is a number")
            index = self.key(item)
        elif type(item) == str:
            print("Item is a string")
            for char in item:
                if item.index(char) == 0:
                    index = ord(char)
                index += ord(char)
                print(index)
                index = self.key(index)
        found = False
        passed = False
        checker = index
        while found == False:
            if index == self.maxsize:
                index = 0
                passed = True   
            if index == checker and passed == True:
                print("Item not found")
            if self.table[index] == item:
                print(self.table)
                print("Item found at index: " + str(index))
                found = True
            else:
                index += 1

    def isFull(self):
        if len(self.table) == self.maxsize:
            return True
        else:
            return False

    def isEmpty(self):
        if len(self.table) == 0:
            return True
        else:
            return False
        
        

h1 = HashTable(6, "folding")
h1.add(3)
h1.add(9)
h1.add("Cool")
h1.add("A")
h1.remove("Cool")
h1.remove(3)
h1.add("Cool")
h1.add("B")
h1.search("B")



