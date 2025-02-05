from .node import NodeWithList
from .page import Page


class Score(NodeWithList):
    """representing the whole score"""
    CHILDNAMES = ["title$", "unitsperstavespacing", "miditempo", "midivelocity", "midilyrics", 
                  "midirepeats", "preedit", "pages"]
    
    def __init__(self, name, value, parent):
        NodeWithList.__init__(self, name, value, parent, [("pages", Page)])
        
        self.title = self.__getitem__("title$")
        
    def accept(self, visitor):
        visitor.visit(self)
        for page in self.getChild("pages"):
            page.accept(visitor)