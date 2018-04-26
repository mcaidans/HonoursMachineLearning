import Node

class Connection:
    Node nodeFrom
    Node nodeTo
    float weight



    def __init__(self, nodeFrom, nodeTo):
        self.nodeFrom = nodeFrom
        self.nodeTo = nodeTo
