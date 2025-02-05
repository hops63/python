import unittest
import sys

from ...src.nodes import node#, value

class NodeTest(unittest.TestCase):
    def testSimple(self):
        """Test access to class members"""
#        node = node.Node("Peter", Value("ist doof"))
        n = node.Node("Peter", "ist doof", None)
        
        
        self.assertEqual(n.getName(), "Peter")
        self.assertEqual(n.getValue(), "ist doof")
        


#===============================================================================
#suite = testsuite.makeLoggingSuite(NodeTest)
#unittest.TextTestRunner(verbosity=2).run(suite)
#===============================================================================
