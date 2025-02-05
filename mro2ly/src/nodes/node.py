import sys
import logging
from .nodelist import NodeList

class Node:
    """Base class for all nodes"""
    CHILDNAMES = []
    printchildren = False

    def __init__(self, name, value, parent):
        self.logger = logging.getLogger("nodes.Node")
        if Node.printchildren:
            cl = []
            for child in value:
                cl.append(child[0])
            print >> sys.stderr, "CHILDNAMES(%s) = " % name, cl
        
        for child in value:
            if child[0] not in self.CHILDNAMES:
                raise UnknownNodeError(child[0], self)

        self._name = name
        self._value = value
        self._parent = parent
        self.logger.debug("new '%s' node created"%(name))
        
        self._dict = self._getValueAsDict()


    def __len__(self):
        return len(self._dict)
        
    def __getitem__(self, key):
        return self._dict[key]
        
    def getName(self):
        return self._name
    
    def getValue(self):
        return self._value
    
    def getParent(self):
        return self._parent
    
    def _getValueAsDict(self):
        dict = {}
        for k, v in self.getValue():
            dict[k] = v
        return dict
        
    def accept(self, visitor):
        self.logger.info("No specific accept handler implemented for node '%s'" % self.__class__)
        visitor.visit(self)
        

class NodeWithList(Node):
    """ Node with a list of childs of the same type"""
    
    __childDict = {}
    
    def __init__(self, name, value, parent, listChildren):
        Node.__init__(self, name, value, parent)
        logger = logging.Logger("nodes.NodeWithList")
        
        for child in listChildren:
            listname, listtype = child
            listChild = self.__makeChildList(listname, listtype)
            self.__childDict[listname] = listChild
        
    def __makeChildList(self, listname, listtype):
        lst = []
        try:
            if listname in self._dict:
                content = self._dict[listname]
                lst = NodeList(listtype, content, self)
        except:
            self.logger.error("no node '%s' found in '%s'"%(listtype, self._name))
            raise

        return lst
        
    def getChild(self, name):
        child = []
        try:
            child = self.__childDict[name]
        except KeyError:
            self.logger.error("No child with name '%s' in node '%s'" % (name, self._name))
            
        return child
        
        
            
class UnknownNodeError(Exception):
    """Exception, that is raised, if an unknown node is found"""
    def __init__(self, node, parent):
        Exception.__init__(self)
        self.__errorNode = node
        self.__parent = parent
        
    def __str__(self):
        return self.errMsg()
    
    def errMsg(self):
        return "Unknown node '%s' found in parent '%s'" % (self.__errorNode, self.__parent)