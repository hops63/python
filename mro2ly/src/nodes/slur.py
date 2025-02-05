from .node import Node

class Slur(Node):
    """Pesentation of a slur"""
    CHILDNAMES =  ['leftpt', 'rightpt', 'radius']
    
    def __init__(self, name, value, parent):
        Node.__init__(self, name, value, parent)
