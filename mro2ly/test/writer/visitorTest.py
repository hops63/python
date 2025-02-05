import sys
import unittest

sys.path.append("../../src")
from writer import decorators

class Base:
    def __init__(self):
        self.name = "Base"
        
    def accept(self, visitor):
        visitor.visit(self)
        
class Child(Base):
    def __init__(self):
        Base.__init__(self)
        self.name = "Child"

class Child2(Base):
    def __init__(self):
        Base.__init__(self)
        self.name = "Child2"

class Visitor:
    used = decorators.PolymorphDecorator()    
    def __init__(self):
        self.retval = ""
    
    def simple_deco(f):
        print("simple_deco")
        return f
        
    def parameter_deco(type_t):
        print("Expected type: %s" % (type_t))
        def decorated(f):
            def tester(self, *args):
                print("Given arguments: %s" % args)
                
                if isinstance(args[0], type_t):
                    return f(self, args[0])
                else:
                    print("Wrong type \n")
            return tester
        return decorated
        
        
    @used.forType(Base)
    #@parameter_deco(Base)
    def visit(self, node):
        self.retval = "in Base? %s" % (node.name)
        

    @used.forType(Child)
    #@parameter_deco(Child)
    def visit(self, node):
        self.retval = "in Child? %s" % (node.name)
        
       
class DecoratorTest(unittest.TestCase):
    def testPolymorphism(self):
        b = Base()
        c = Child()
        c2 = Child2()
        v = Visitor()
    
        b.accept(v)
        self.assertEqual("in Base? Base", v.retval)
        c.accept(v)
        self.assertEqual("in Child? Child", v.retval)


#===============================================================================
sys.path.append("..")
import testsuite
suite = testsuite.makeLoggingSuite(DecoratorTest)
unittest.TextTestRunner(verbosity=2).run(suite)
#===============================================================================
