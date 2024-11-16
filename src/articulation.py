class ArticulationPointFinder():

    def __init__(self, graph) -> None:
        #self.is_articulation_point = [False] * len(graph.adj)
        self.graph = graph

    # [[3, 2, 1], [0], [3, 0, 4], [0, 2], [2]]
    def dfs(self, start = 0):
        if len(self.graph) == 0:
            return None
        
        adj = []
        stack = [start]
        visited = set()
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                adj.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

        return adj  




def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
    

if __name__ == "__main__": 
    graph1 = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
    graph2 = [[2,3,1], [0], [0,4], [0], [2]]
    graph3 = [[3, 2, 1], [0], [3, 0, 4], [0, 2], [2]]

    A = ArticulationPointFinder(graph3)
    print(A.dfs())  

