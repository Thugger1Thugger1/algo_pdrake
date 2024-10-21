class Node():
    def __init__(self, item) -> None:
        self.item = item
        self.next = None
    
    def addItem(self, item):
        newNode = Node(item)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def delNode(self, item):
        curr = self.head
        if self.head is None:
                return None
        if self.head == item:
            self.head.next = self.head

        while curr.next != None:
            if curr.item == item:
               curr.next = curr.next.next
            curr = curr.next

