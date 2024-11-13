class IndexMinPQ():

    def __init__(self):
        self.heap = []
        self.size = 0
        self.dict = {}

    def parent(self, pos): 
        return (pos -1)//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos + 1
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 2
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        return pos*2 > self.size 

    # Swap two given positions
    def swap(self, posOne, posTwo):
        A = self.heap[posOne][0]
        B = self.heap[posTwo][0]
        self.heap[posOne], self.heap[posTwo] = self.heap[posTwo], self.heap[posOne]
        self.dict[A], self.dict[B] = self.dict[B], self.dict[A]

    # Take a given position and and recursively swap
    def heapify(self, pos):
        
        print('calling heapify', self.heap)

        if not self.isLeaf(pos):

            left = self.leftChild(pos)
            right = self.rightChild(pos)
            # if the either the left or right child position contains a child 
            # and either left or right child is smaller than the current pos enter
            if (left < self.size and self.heap[pos][1] > self.heap[left][1]) or \
                (right < self.size and self.heap[pos][1] > self.heap[right][1]): 
                
                # if the left child doesn't exist, neither does the right
                # if left >= self.size:
                #     pass
                # if the right child doesn't exist, swap the left with pos
                if right >= self.size:
                    self.swap(pos, left)
                    
                
                elif self.heap[left][1] < self.heap[right][1]:
                    self.swap(pos, left)
                    self.heapify(left)
                else: 
                    self.swap(pos, right)
                    self.heapify(right)

    def is_empty(self):
        return self.size == 0

    def enqueue(self, key, priority):
        self.size += 1
        self.heap.append([key, priority])
        self.dict[key] = self.size - 1
        self.dict
        current = self.size - 1

        while current > 0 and self.heap[current][1] < self.heap[self.parent(current)][1]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        
        print(self.size)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty priority queue")
        root = self.heap[0]
        self.swap(0, -1)
        self.heap.pop()
        self.size -= 1
        if not self.is_empty():
            self.heapify(0)

        
        return root[0]

    def reduce_priority(self, key, priority):
        print('calling reduce priority', self)
        print(self.dict)
        current = self.dict[key]
        self.heap[self.dict[key]][1] = priority
        #print('calling reduce priority', self.heap)
        while current > 0 and self.heap[current][1] < self.heap[self.parent(current)][1]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        #print(self.dict[key])
        self.dict[key] = priority
        #print(self.dict)

    def __str__(self) -> str:
        
        return str(self.heap) + str(self.size)

if __name__ == "__main__":
    N = IndexMinPQ()
    N.enqueue('a', 2)
    N.enqueue('b', 1)
    N.enqueue('c', 0)
    N.enqueue('d', -1)
    N.dequeue()
    N.reduce_priority('a', -2)
    print(N)
    