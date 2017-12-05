class Node:
    def __init__(self,state,parent,depth,operator):
        self.state=state
        self.parent=parent
        self.depth=depth
        self.operator = operator
        self.fn=-1