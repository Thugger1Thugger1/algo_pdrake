class IndexMinPQ():

    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, pos): 
        return pos//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos 
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        return pos*2 > self.size 

    # Swap two given positions
    def swap(self, posOne, posTwo):
        self.heap[posOne], self.heap[posTwo] = self.heap[posTwo], self.heap[posOne]

    # Take a given position and and recursively swap
    def heapify(self, pos):

        if not self.isLeaf(pos):

            if self.heap[pos][1] > self.heap[self.leftChild(pos)][1] or self.heap[pos][1] > self.heap[self.rightChild(pos)][1]: 
                
                if self.heap[self.leftChild(pos)][1] < self.heap[self.rightChild(pos)][1]:
                    self.swap(pos, self.leftChild(pos))
                    self.heapify(self.leftChild(pos))
                else: 
                    self.swap(pos, self.rightChild(pos))
                    self.heapify(self.rightChild(pos))

    def is_empty(self):
        return self.size == 0

    def enqueue(self, key, priority):
        self.size += 1
        self.heap.append([key, priority])
        current = self.size - 1

        while current > 0 and self.heap[current][1] < self.heap[self.parent(current)][1]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty priority queue")
        root = self.heap[0]
        self.swap(0, -1)
        self.heap.pop()
        self.size -= 1
        if not self.is_empty:
            self.heapify(0)
        
        return root[0]

    def reduce_priority(self):
        pass

    def __str__(self) -> str:
        return str(self.heap)

if __name__ == "__main__":
    N = IndexMinPQ()
    N.enqueue('a', 2)
    N.enqueue('b', 1)
    N.enqueue('c', 0)
   
    print(N.dequeue())
    print(N.dequeue())
    print(N.dequeue())
    print(N)
    