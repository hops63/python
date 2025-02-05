from .node import Node
from .fileheader import Fileheader
from .score import Score

class Document(Node):
    CHILDNAMES = ["SharpEyeMusicOCROutputFile", "fileheader", "score"]
    
    
    def __init__(self, nodelist):
        Node.__init__(self, "document", nodelist, None)
        
        for name, subnodes in self.getValue():
            if name == self.CHILDNAMES[0]:
                pass
            elif name == self.CHILDNAMES[1]:
                self.fileheader = Fileheader(name, subnodes, self)
            elif name == self.CHILDNAMES[2]:
                self.score = Score(name, subnodes, self)

    def __str__(self):
        return "Document with %d pages" % (len(self.score.getChild("pages")))
        
    def getInfo(self):
        print("Document info:")
        pages = self.score.getChild("pages")
        print("   Pages:\t%d"%(len(pages)))
        print("   Systems:\t%d"%(reduce( lambda x,y:x+y, [len(k.getChild("systems")) for k in pages])))
        
        
    def accept(self, visitor):
        visitor.visit(self)
        self.fileheader.accept(visitor)
        self.score.accept(visitor)
        

