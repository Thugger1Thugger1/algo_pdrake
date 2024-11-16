class IndexMinPQ():
    # this class should have no issues with only using a two-item list
    # because i access each priority directly rather than using the whole list

    def __init__(self):
        self.heap = []
        self.size = 0
        self.dict = {}

    def parent(self, pos): 
        return (pos -1)//2
  
    # return the pos of left child in relation to passed node
    def leftChild(self, pos): 
        return 2 * pos + 1
  
    # return the pos of right child in relation to passed node
   
    def rightChild(self, pos): 
        return (2 * pos) + 2
  
    # return true if pos of passed node is a leaf
    def isLeaf(self, pos): 
        return pos*2 > self.size 

    # swap posOne and posTwo in the heap
    # swap posOne and posTwo in the dictionary
    def swap(self, posOne, posTwo):
        A = self.heap[posOne][0]
        B = self.heap[posTwo][0]
        self.heap[posOne], self.heap[posTwo] = self.heap[posTwo], self.heap[posOne]
        self.dict[A], self.dict[B] = self.dict[B], self.dict[A]

    # take a passed node and recursively sink to the bottom
    # some of this is probably redundant
    def sink(self, pos):

        if not self.isLeaf(pos):

            left = self.leftChild(pos)
            right = self.rightChild(pos)
            # if the either the left or right child position contains a node
            # and either left or right child is smaller than the current pos enter
            if (left < self.size and self.heap[pos][1] > self.heap[left][1]) or \
            (right < self.size and self.heap[pos][1] > self.heap[right][1]): 
                
                # if the left child doesn't exist, neither does the right
                # if the right child doesn't exist, swap the left with pos
                if right >= self.size:
                    self.swap(pos, left)
                    
                
                # else if the right childs priority is greater than the left child swap the left with pos
                elif self.heap[left][1] < self.heap[right][1]:
                    self.swap(pos, left)
                    self.sink(left)
                # otherwise, the right child must exist and be smallest so swap with pos
                else: 
                    self.swap(pos, right)
                    self.sink(right)

    def is_empty(self):
        return self.size == 0

    # append a list of values key, priority to the heap and add the index of the key to the dict
    def enqueue(self, key, priority):
        self.size += 1
        self.heap.append([key, priority])
        self.dict[key] = self.size - 1
        current = self.size - 1

        # while current node is not the root node and priority of current node is less than parents
        # swap current node with parent node than set current node to parent node
        while current > 0 and self.heap[current][1] < self.heap[self.parent(current)][1]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # swap first and last nodes, pop the now last node (previously first node)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty priority queue")
        root = self.heap[0]
        self.swap(0, -1)
        self.heap.pop()
        self.size -= 1
        # resort heap
        if not self.is_empty():
            self.sink(0)

        
        return root[0]


    def reduce_priority(self, key, priority):
        current = self.dict[key]
        self.heap[self.dict[key]][1] = priority
        while current > 0 and self.heap[current][1] < self.heap[self.parent(current)][1]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        self.dict[key] = priority


    def __str__(self) -> str:
        
        return str(self.heap) + str(self.size)

    def __bool__(self):
        return self.size > 0

    def display(self):
        pass

if __name__ == "__main__":
    N = IndexMinPQ()
    N.enqueue('a', 2)
    N.enqueue('b', 2)
    N.enqueue('c', 0)
    N.enqueue('d', -1)
    print(N)
