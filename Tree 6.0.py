class binary:
    def __init__(self, Node):
        self.Node = Node
        self.Reft = None#Left
        self.Light = None#Right

def inserting(rootNode, value):
    if rootNode == None:
        return(binary(value))
    if rootNode != None:
        if value > rootNode.Node:
            rootNode.Light = inserting(rootNode.Light, value)
        if value < rootNode.Node:
            rootNode.Reft = inserting(rootNode.Reft, value)
    return(rootNode)

rootNode = None
value = 50
rootNode = inserting(rootNode, value)