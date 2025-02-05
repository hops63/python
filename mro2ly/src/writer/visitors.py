import logging
import sys

import .decorators

sys.path.append("..")

from .nodes import *
"""
from .nodes.node import Node
from .fileheader import Fileheader
from .document import Document
from .score import Score
from .page import Page
"""

class NodeVisitor:
    used = decorators.PolymorphDecorator()
    
    def __init__(self):
        self.nodeCount = 0
    
    def __incrementCounter(self):
        self.nodeCount = self.nodeCount +1

     
    @used.forType(node.Node) 
    def visit(self, node):
        self.__incrementCounter()
        
    @used.forType(document.Document)    
    def visit(self, node):
        print("Visit Document node...")
        self.__incrementCounter()

    @used.forType(fileheader.Fileheader)    
    def visit(self, fileheader):
        print("Visit FileHeader node...")
        self.__incrementCounter()

    @used.forType(score.Score)    
    def visit(self, score):
        print("Visit Score node...")
        self.__incrementCounter()
        
    @used.forType(page.Page)
    def visit(self, page):
        print("Visit Page node ...")
        self.__incrementCounter()

    def __str__(self):
        return "NodeVisitor: nodeCount = %d" % (self.nodeCount)
        
class BarVisitor(NodeVisitor):
    used = decorators.PolymorphDecorator()
    bars = {}
    
    @used.forType(bar.Bar)
    def visit(self, bar):
        self.bars[bar.getID()] = bar 