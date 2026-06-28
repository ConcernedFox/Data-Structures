class tree:
    def __init__(self, Node):
        self.Node = Node
        self.Left = None
        self.Right = None

Numbers = tree(10)
Numbers.Left = tree(5)
Numbers.Right = tree(15)

def count(Node):
    if Node == None:
        return(0)
    return 1 + count(Node.Left) + count(Node.Right)

print(count(Numbers))
    