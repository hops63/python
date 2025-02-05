from .node import Node


class Fileheader(Node):
    """representing the fileheader"""
    CHILDNAMES = ["version", "characterencoding"]
    
    def __init__(self, name, nodelist, parent):
        Node.__init__(self, name, nodelist, parent)
        
        self.version = self._dict.get(self.CHILDNAMES[0], "1000")
        self.encoding = self._dict.get(self.CHILDNAMES[1], "ASCII")

        
         
            