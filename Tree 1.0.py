class tree:
    def __init__(self, Node, Left, Right):
        self.Node = Node
        self.Left = Left
        self.Right = Right


Numbers = tree(1, 2, 3)
Numbers.Left = tree(2, 4, 5)
Numbers.Right = tree(3, 6, 7)