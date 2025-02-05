import unittest
import sys

sys.path.append("../../src")

from nodes import nodelist, node

class NodeListTest(unittest.TestCase):
    def testSimple(self):
        """Test reading an NodeList"""
        nl = nodelist.NodeList(TestNode, 
                    [('nof', '1'), ('Page', [('height', '23')])], None)
                
        self.assertEqual(len(nl), 1)
        self.assertEqual(nl[0]["height"], '23')

        loopCheck = False
        for k in nl:
            loopCheck = True
            self.assertEqual(k["height"], '23')
            
        self.assertTrue(loopCheck, "access with for loop not tested")

class TT:        
    def testUnvalidArray(self):
        """Test reading invalid NodeList"""
        nl = nodelist.NodeList()
        self.assertRaises(nodelist.UnvalidArrayError, nodelist.NodeList.__init__, 
                          nl, TestNode, [('Page', [('height', '23')])], None)

        self.assertRaises(nodelist.UnvalidArrayError, nodelist.NodeList.__init__, 
                          nl, TestNode, [('size', '4'), ('Page', [('height', '23')])], None)
       
        
    def testThreePages(self):
        """Test reading three page entries into nodelist"""
        nl = nodelist.NodeList(TestNode, 
                    [('nof', '3'), 
                    ('Page', [('height', '10')]), 
                    ('Page', [('height', '20')]), 
                    ('Page', [('height', '30')])], None)
          
      
        self.assertEqual(len(nl), 3)
        self.assertEqual(nl[0]["height"], '10')
        self.assertEqual(nl[2]["height"], '30')
  
  
  
class TestNode(node.Node):
    CHILDNAMES=["height"]
    
    def __init__(self, name, children, parent):
        node.Node.__init__(self, name, children, parent)
        

       
#===============================================================================
sys.path.append("..")
import testsuite
suite = testsuite.makeLoggingSuite(NodeListTest)
unittest.TextTestRunner(verbosity=1).run(suite)
#===============================================================================
