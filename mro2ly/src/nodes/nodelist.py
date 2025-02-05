import logging

class NodeList(list):
    def __init__(self, nodetype=object, nodevalue=[('nof', '0')], parent=None):
        self.logger = logging.getLogger("nodes.NodeList")
        self.logger.debug("new NodeList for type '%s'"%nodetype)
        size = nodevalue[0]
        if size[0] != 'nof':
            raise UnvalidArrayError("Expected NodeList does not start with 'nof' tuple!", parent)

        count = int(size[1])
        try:
            for name, content in nodevalue[1:]:
                item = nodetype(name, content, parent)
                list.append(self, item)
        except:
            self.logger.error("can not append instance of type '%s' to list"%nodetype)
            raise

        if len(self) != count:
            self.logger.error("%d list items defined, but %d found" % (count, len(self)))
            
    

class UnvalidArrayError(Exception):	
    """Exception, that is raised, if an array is not recognized correctly"""
    def __init__(self, msg, parent):
        Exception.__init__(self)
        self.__msg = msg
        self.__parent = parent

    def __str__(self):
        return self.errMsg()
    
    def errMsg(self):
        return "'%s' in parent '%s'" % (self.__msg, self.__parent)
    