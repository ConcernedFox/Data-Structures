class graph:
    def __init__(self, n):
        self.n = n
        self.adjacency = []
        for i in range(n):
            self.adjacency.append([])
        print(self.adjacency)
    def createEdge(self, x, y):
        self.adjacency[x-1].append(y)
        self.adjacency[y-1].append(x)


road = graph(4)
road.createEdge(1, 2)
print(road.adjacency)
road.createEdge(1, 3)
print(road.adjacency)
road.createEdge(1, 4)
print(road.adjacency)
road.createEdge(2, 3)
print(road.adjacency)
road.createEdge(2, 4)
print(road.adjacency)
road.createEdge(3, 4)
print(road.adjacency)