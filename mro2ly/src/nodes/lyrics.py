from .node import NodeWithList, Node


class LyricLine(NodeWithList):
    CHILDNAMES =  ['abot', 'height', 'elements']

    def __init__(self, name, value, parent):
        NodeWithList.__init__(self, name, value, parent, 
            [("elements", LyricElement)])



class LyricElement(Node):
    CHILDNAMES =  ['extender', 'c0', 'c1', 'text$', 'midc']
    
    def __init__(self, name, value, parent):
        Node.__init__(self, name, value, parent)
        
        
        
class Text(Node):
    CHILDNAMES = ['abot', 'c0', 'height', 'style', 'type', 'text$']
    
    def __init__(self, name, value, parent):
        Node.__init__(self, name, value, parent)
        
        
class Dynamic(Node):
    CHILDNAMES = ['type', 'c', 'c0', 'c1', 'r']
    
    def __init__(self, name, value, parent):
        Node.__init__(self, name, value, parent)
                