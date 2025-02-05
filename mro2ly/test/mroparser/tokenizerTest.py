import unittest
import types
import sys

sys.path.append("../../src")
sys.path.append("..")

from mroparser import tokenizer

class ListTester(unittest.TestCase):
	def __init__(self, val):
		self.expected = val

	def check(self, actual):
		print(actual)
		self.assertEqual(len(self.expected), len(actual))
		i = 0
		for tok in self.expected:
			self.assertEqual(tok, actual[i])
			i = i+1

		
class TokenizerTest(unittest.TestCase):
    def setUp(self):
        self.tokenizer = tokenizer.Tokenizer()

    def testSimple(self):
        """Tokenizing simple values"""
        content = 'name$ "Hier ist nichts" wert1 1/3'
        expected = ['name$', 'Hier ist nichts', 'wert1', '1/3']
        tree = self.tokenizer.parse(content)
        self.assertEqual(expected, tree)
	
    def testSimpleString(self):
        """Tokenizing simple values with strings as last value"""
        content = 'wert1 1/3 name$ "Hier ist nichts"'
        expected = ['wert1', '1/3', 'name$', 'Hier ist nichts']
        tree = self.tokenizer.parse(content)
        self.assertEqual(expected, tree)

        content = 'newName$ "Hier ist gar nichts"'
        expected = ['newName$', 'Hier ist gar nichts']
        tree = self.tokenizer.parse(content)
        self.assertEqual(expected, tree)
	
    def testSimpleQuotedString(self):
        """Tokenizing simple values with a quoted string as last value"""
        content = 'wert1 1/3 name$ "Hier ist ""gar"" nichts"'
        expected = ['wert1', '1/3', 'name$', 'Hier ist "gar" nichts']
        tree = self.tokenizer.parse(content)
        self.assertEqual(expected, tree)

    def testLeadingSpace(self):
        """Test leading whitespaces"""
        content = 'start " space left" end'
        expected = ['start', 'space left', 'end']
        tree = self.tokenizer.parse(content)
        self.assertEqual(expected, tree)
		
		
    def testTrailingSpace(self):
        """Test trailing whitespaces"""
        content = 'start "space right " end'
        expected = ['start', 'space right', 'end']

        tree = self.tokenizer.parse(content)
        self.assertEqual(expected, tree)
		
    def testInnerQuotation(self):
        """Test stacked quotations"""
        content = 'start "outer ""inner quot"" outer again" end'
        expected = ['start', 'outer "inner quot" outer again', 'end']

        tree = self.tokenizer.parse(content)
        self.assertEqual(expected, tree)
		
    def testLeadingInnerQuotation(self):
        """Test a leading inner quotation"""
        content = 'start " ""inner quot"" outer" end'
        expected = ['start', '"inner quot" outer', 'end']
        tree = self.tokenizer.parse(content)
        self.assertEqual(expected, tree)

        content = 'start """inner quot"" outer" end'
        expected = ['start', '"inner quot" outer', 'end']
        tree = self.tokenizer.parse(content)
        self.assertEqual(expected, tree)

    def testTrailingInnerQuotation(self):
        """Test a trailing inner quotation"""
        content = 'start "outer ""inner quot"" " end'
        expected = ['start', 'outer "inner quot"', 'end']
        tree = self.tokenizer.parse(content)
        self.assertEqual(expected, tree)
		
        content = 'start "outer ""inner quot""" end'
        expected = ['start', 'outer "inner quot"', 'end']
        tree = self.tokenizer.parse(content)
        self.assertEqual(expected, tree)

    def _testRead(self):
        """Test Reading an entire MRO file"""
        mroFile = open("../reel2.mro", 'r')
        tree = self.tokenizer.parse(mroFile.read())

        print(tree)
        self.assertTrue(len(tree) != 0)
		
#===============================================================================
import testsuite
#suite = testsuite.LoggingTestSuite()
#suite.addTest(TokenizerTest("testLeadingInnerQuotation"))
suite = testsuite.makeLoggingSuite(TokenizerTest)
#suite.addTest(TokenizerTest("_testRead"))
unittest.TextTestRunner(verbosity=2).run(suite)

#===============================================================================