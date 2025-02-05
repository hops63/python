from .node import NodeWithList
from .system import System

class Page(NodeWithList):
    """One side of musical notation"""
    CHILDNAMES = ["width", "height", "origwidth", "origheight", "skewangle",
                    "rowoffset", "coloffset", "spacing", "imagefpath$", "systems"]

    def __init__(self, name, value, parent):
        NodeWithList.__init__(self, name, value, parent, [("systems", System)])
        
        
    def accept(self, visitor):
        visitor.visit(self)
