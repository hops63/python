from .node import Node, NodeWithList
from .nodelist import NodeList
from .chord import Chord
from .clef import Clef



class Bar(NodeWithList):
    CHILDNAMES =  ['clefs', 'timesig', 'chords', 'barline', 'keysigs']  
    
    def __init__(self, name, value, parent):
        NodeWithList.__init__(self, name, value, parent, 
            [("chords", Chord), ("clefs", Clef), ("keysigs", KeySig)])

            
class BarLine(Node):
    SHAPES = ['Single', 'Double', 'Leftrepeat', 'Rightrepeat', 'Backtobackrepeat']
    
    def __init__(self, name, value, parent):
        Node.__init__(self, name, value, parent)
                      
                      
class TimeSig(Node):
    CHILDNAMES = ['showasalpha', 'top', 'bottom', 'centre', 'timeslice']
    
    def __init__(self, name, value, parent):
        Node.__init__(self, name, value, parent)
                      

class KeySig(Node):
    CHILDNAMES = ['key', 'centre']
    
    def __init__(self, name, value, parent):
        Node.__init__(self, name, value, parent)
                      