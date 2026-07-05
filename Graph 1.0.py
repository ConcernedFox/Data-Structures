class graph:
    def __init__(self, n):
        self.n = n
        self.adjacency = []
        for i in range(n):
            self.adjacency.append([])

    def createEdge(self, n):