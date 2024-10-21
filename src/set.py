#add
#remove
#contain

class SetList():
    def __init__(self):
        self.ls = []

    def add(self, item):
        exists = False
        for x in self.ls:
            if item == x:
                return
        self.ls.append(item)

    
    def remove(self, item):
        for x in self.ls:
            if item == x:
                self.ls.remove(x)
    
    def contains(self, item):
        for x in self.ls:
            if item == x:
                return True
        return False

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class SetLinked():
    def __init__(self):
        self.top = None

    def contains(self, value):
        current = self.top
        while current:
            if value == current.item:
                return True
            current = current.next
        return False

    def add(self, value):
        if not self.contains(value):
            self.top = Node(value, self.top)

    def remove(self, value):
        if self.contains(value):
            node = previous = self.top
            if node.item == value:
                self.top = node.next
            while node:
                if node.item == value:
                    previous.next = node.next
                    return
                previous = node
                node = node.next
    
    def __str__(self): 
        current = self.top
        s = []
        while current:
            s.append(str(current.item))
            current = current.next  
        return f"<{', '.join(s)}>"

    
        
    def addList(self, list):
        for x in list:
            self.add(x)

ls = SetLinked()
ls.addList([1,2,3,4,5,5,5,6,6,7])
print(ls)
ls.remove(7)
print(ls)


#Direct Addressing Table, fastest way to store short list of small positive ints
class DAT():
    def __init__(self):
        self.keys = [False] * 100
    
    def add(self, item):
        self.keys[item] = True

    def remove(self, item):
        self.keys[item] = False
    
    def contains(self, item):
        return self.keys[item]

    def __str__(self): 
        s = []
        i = 0
        for x in self.keys:
            if x == True:
                s.append(str(i)) 
            i += 1
        return f"<{', '.join(s)}>"