from .node import Node, NodeWithList
from .note import Note

class Chord(NodeWithList):
    CHILDNAMES =  ['virtualstem', 'stemup', 'tuplettransform', 'tupletcount', 
                   'staccato', 'tenuto', 'pause', 'accent', 'naugdots', 'nflags', 
                   'flagposn', 'headend', 'beam', 'notes']
    
    def __init__(self, name, value, parent):
        NodeWithList.__init__(self, name, value, parent, 
            [("notes", Note)])
        
        self.beam = Beam(self.__getitem__('beam'), self)




class Beam(Node):
    CHILDNAMES = ['id', 'nofnodes', 'nofleft', 'nofright']
    
    def __init__(self, children, parent):
        Node.__init__(self, 'beam', children, parent)