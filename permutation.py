class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.next = None

class HashTable: 
    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key): 
        return hash(key) % self.capacity 

    def insert(self, key, value): 
        index = self._hash(key) 

        if self.table[index] is None: 
            self.table[index] = Node(key, value) 
            self.size += 1
        else: 
            current = self.table[index] 
            while current: 
                if current.key == key: 
                    current.value = value 
                    return
                current = current.next
            new_node = Node(key, value) 
            new_node.next = self.table[index] 
            self.table[index] = new_node 
            self.size += 1

    def search(self, key): 
        index = self._hash(key) 
 
        current = self.table[index] 
        while current: 
           if current.key == key: 
               return current.value 
           current = current.next
        raise KeyError(key)

    def __str__(self): 
        elements = [] 
        for i in range(self.capacity): 
            current = self.table[i] 
            while current: 
                elements.append((current.key, current.value)) 
                current = current.next
        return str(elements) 


#given two strings, define a function that tells you if one is a perm of the other

# 1 -> a
# 2 -> ab, ba
# 3 -> ab, ba, cab, acb, abc, cba, bca, bac
def checkPerm(first, second):

    hash_table = HashTable(capacity=100)

    def rec(s):
        if len(s) == 1:
            return [s]       # recursive case

        last = s[-1]         # Chop off the last character
        remaining = s[:-1]   # remaining characters

        perms = rec(remaining) # recursively get all remaining perms of string

        result = []

        for perm in perms:
            for i in range(len(perm) + 1):
                # Create a new permutation by inserting `last` in position `i`
                new_perm = perm[:i] + last + perm[i:]
                result.append(new_perm)
                hash_table.insert(new_perm, new_perm)

        return result
    rec(second)
    if hash_table.search(first):
        return True
    return False
