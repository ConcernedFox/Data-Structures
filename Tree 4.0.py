class tree:
    def __init__(self, Node):
        self.Node = Node
        self.Left = None
        self.Right = None

def inorder(Node):
    if Node.Left != None:
        inorder(Node.Left)
    print(Node.Node)
    if Node.Right != None:
        inorder(Node.Right)

def preorder(Node):
    print(Node.Node)
    if Node.Left != None:
        preorder(Node.Left)
    if Node.Right != None:
        preorder(Node.Right)

def postorder(Node):
    if Node.Left != None:
        postorder(Node.Left)
    if Node.Right != None:
        postorder(Node.Right)
    print(Node.Node)

Numbers = tree(1)
Numbers.Left = tree(2)
Numbers.Right = tree(3)
Numbers.Left.Left = tree(4)
Numbers.Left.Right = tree(5)
Numbers.Right.Left = tree(6)
Numbers.Right.Right = tree(7)
print("This is Inorder Traversal")
inorder(Numbers)
print("This is Preorder Traversal")
preorder(Numbers)
print("This is Postorder Traversal")
postorder(Numbers)