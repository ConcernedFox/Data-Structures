class tree:
    def __init__(self, Node):
        self.Node = Node
        self.Left = None
        self.Right = None

Numbers = tree(50)
Numbers.Left = tree(25)
Numbers.Right = tree(75)
Numbers.Left.Left = tree(12)
Numbers.Left.Right = tree(38)
Numbers.Right.Left = tree(62)
Numbers.Right.Right = tree(88)

while Numbers.Right != None:
    Numbers = Numbers.Right
if Numbers.Right == None:
    Numbers.Right = Numbers
    print(str(Numbers.Node) + " is the largest value in this tree, sorted out by inorder traversal, 12, 25, 38, 50, 62, 75, 88")