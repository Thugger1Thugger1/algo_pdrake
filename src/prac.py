heap = []
heap = heap + [['a', 3]]
heap = heap + [['b', 2]]
heap = heap + [['c', 1]]

print(heap[2][0])

if heap[2][1] < heap[1][1]:
    print("True")