#!/usr/bin/python

import sys, os
import logging
from mroparser import treebuilder

class Mro2LyConverter :
    def readFile(self, filename) :
        try :
            file = open(filename, 'r')
        except IOError:
            print("Could not open file: " + filename)
            print(str(sys.exc_info()[1]))
            sys.exit(1)
            
        treeBuilder = treebuilder.TreeBuilder()
        return treeBuilder.parseNodes()
        
    def parse(self):
        pass
    
    def writeFile(self):
        pass
    
    def printHelp(self):
        print("mro2ly -- converts MRO files to Lilypond files")
        print("")
        print("Syntax: mro2ly mrofile")
        print("")
    

    def run(self):
        if len(sys.argv) <= 1:
            self.printHelp()
            sys.exit(0)
        
        infile = sys.argv[1]
        outfile = infile.split(os.sep)[-1].split('.')[0] + ".ly"
        print("Converting '%s' to '%s'" % (infile,outfile))
                
        tree = self.readFile(infile)
        print tree
        self.parse(tree)
	
        self.writeFile(outfile)
        


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    mroParser = Mro2LyConverter()
    mroParser.run()
    
    

