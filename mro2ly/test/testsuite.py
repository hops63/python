import unittest
import logging
import sys

class LoggingTestSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self)
        initLogging()
        
        
def makeLoggingSuite(clazz, prefix="test"):
    suite = unittest.makeSuite(clazz, prefix)
    initLogging()
    
    return suite
    
def initLogging():    
    logging.basicConfig(level=logging.DEBUG, 
                        format="%(levelname)s   %(name)s - %(msg)s",
                        )


    for name in ["nodes.Node", "nodes.NodeList"]:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

