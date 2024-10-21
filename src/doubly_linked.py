class Node:
    def __init__(self, item, next=None, last=None):
        self.item = item
        self.next = next
        self.last = last

class DoublyLinkedList:
    def __init__(self):
        self.header = Node(0)
        self.header.next = self.header
        self.header.last = self.header
        
    
    def __str__(self): 
        current = self.header.next
        s = []
        while current != self.header:
            s.append(str(current.item))
            current = current.next  
        return f"<{', '.join(s)}>"
    

    def add_front(self, item):
        new_node = Node(item)
        new_node.next = self.header.next
        new_node.last = self.header
        self.header.next.last = new_node
        self.header.next = new_node
            
            
    def add_back(self, item):
        new_node = Node(item)
        new_node.next = self.header
        new_node.last = self.header.last
        self.header.last.next = new_node
        self.header.last = new_node


    def addList(self, list):
            for x in list:
                self.add_back(x)

    def remove_front(self):
        self.header.next = self.header.next.next
        self.header.next.last = self.header
        


    def remove_back(self):
        self.header.last = self.header.last.last
        self.header.last.next = self.header
        

    def concatenate(self, other):
        other.header.next.last = self.header.last
        self.header.last.next = other.header.next
        self.header.last = other.header.last
        self.header.last.next = self.header


    def str_reverse(self):
        current = self.header.last
        s = []
        while current != self.header:
            s.append(str(current.item))
            current = current.last  
        return f"<{', '.join(s)}>"

    def contains(self, value):
        current = self.header.next
        while current != self.header:
            if current.item == value:
                return True
            current = current.next
        return False

    def remove(self, value):
        if self.contains(value):
            node = previous = self.header.next
            if node.item == value:
                self.header.next = node.next
            while node != self.header:
                if node.item == value:
                    previous.next = node.next
                    node.next.last = previous
                node = node.next
                previous = node.last
            
    # def reverse(self):
    #     if self.header.next is None: 
    #         return self 
    #     n = self.header.next

    #     lastNode = n.last
    #     n.last = n.next
    #     n.next = lastNode

    #     self.header.last = n

    #     while n != self.header:
    #         lastNode = n.last
    #         n.last = n.next
    #         n.next = lastNode

    #         n = n.last
        
    #     self.header.next = n
    def reverse(self):
        if self.header.next == self.header or self.header.next.next == self.header:
            return
        n = self.header.next

        while n != self.header:
            n.next, n.last = n.last, n.next
            n = n.last

        self.header.next, self.header.last = self.header.last, self.header.next





ls = DoublyLinkedList()
ls.addList([8, 8,9, 8])
print(ls)
ls.remove(8)
print(ls)

