class Node:
    def __init__(self, item, next=None, last=None):
        self.item = item
        self.next = next
        self.last = last

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self): 
        current = self.head
        s = []
        while current:
            s.append(str(current.item))
            current = current.next  
        return f"<{', '.join(s)}>"
    

    def add_front(self, item):
            new_node = Node(item)
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.tail.last = new_node
                self.head = new_node

                


    def add_back(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.last = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_front(self):

        if self.head == self.tail:
            self.head = None
            self.tail = None
        if self.head:
            self.head = self.head.next
            self.head.last = None
        else:
            return


    def remove_back(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        if self.tail:
            self.tail = self.tail.last
            self.tail.next = None
        else:
            return

    def concatenate(self, other):
        if self.tail:
            other.head.last = self.tail
            self.tail.next = other.head
        else:
            return

            
