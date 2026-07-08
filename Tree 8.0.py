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

while Numbers.Left != None:
    Numbers = Numbers.Left
if Numbers.Left == None:
    Numbers.Left = Numbers
    print(str(Numbers.Node) + " is the smallest value in this tree, sorted out by inorder traversal, 12, 25, 38, 50, 62, 75, 88")