import unittest
import types
import sys

sys.path.append("../../src")
sys.path.append("..")

from mroparser import treebuilder
from nodes import document
from writer import visitors

class TreeBuilderTest(unittest.TestCase):
    def setUp(self):
        self.treebuilder = treebuilder.TreeBuilder()

    def testSimpleValue(self):
        """read a sequence of simple values"""
        sequence = 'item1 value1 item2 "a string value"'
        tree = self.treebuilder.parseNodes(sequence)
        self.outputTree(tree)
    
    def testRead(self):
        """read and parse an entire MRO file"""
        mroFile = open("../reel2.mro", 'r')
        tree = self.treebuilder.parseNodes(mroFile.read())
        print(tree[:2])
#        self.outputTree(tree)

    def outputTree(self, tree):
        print("Number of top level values in tree: %d" % (len(tree)))
        for tag in tree:
            self.output("",tag)

        self.assertTrue(len(tree) != 0)

    def output(self, space, tag):
        if type(tag[1]) == types.ListType:
            print("".join((space, tag[0])))
            for subtag in tag[1]:
                self.output("   "+space, subtag)
        else:
            print("".join((space, ", ".join(tag))))


    def testBuildDocument(self):
        """Build document out of parsed file"""
        mroFile = open("../reel2.mro", 'r')
        tree = self.treebuilder.parseNodes(mroFile.read())

        doc = document.Document(tree)

        print(doc.getInfo())
        
        #"""Iterate with visitor over all nodes"""
        visitor = visitors.NodeVisitor()
        doc.accept(visitor)
        
        print(visitor)
        

    
      
#===============================================================================
from nodes import node
import testsuite, sys
node.Node.printchildren=False

runAll = False
if (runAll==True):
    suite = testsuite.makeLoggingSuite(TreeBuilderTest)
else:
    suite = testsuite.LoggingTestSuite()

    #suite.addTest(TreeBuilderTest("testRead"))
    suite.addTest(TreeBuilderTest("testBuildDocument"))
    
unittest.TextTestRunner(verbosity=2).run(suite)
#===============================================================================
