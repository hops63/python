from .node import NodeWithList
from .nodelist import NodeList
from .slur import Slur
from .stave import Stave

class System(NodeWithList):
    CHILDNAMES = ['top', 'left', 'width', 'height', 'staves', 'slurs']
    
    def __init__(self, name, value, parent):
        NodeWithList.__init__(self, name, value, parent, 
            [("staves", Stave), ("slurs", Slur)])
        
        
       
    
