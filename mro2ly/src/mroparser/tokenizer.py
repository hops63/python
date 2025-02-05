class Tokenizer:
    def _CheckSentence(self, inString):
        if inString:
            self.newTree.append(" ".join(self.buffer))
            del self.buffer[:]
        return not inString

    
    def parse(self, src):
        """Parse the given string (src) and return a list of tokens"""
        self.newTree = []
        self.buffer = []

        inString = True
        inQuote = False
        quote = []
        countSimple = 0
        countComplex = 0
        
        for tok in src.split('"'):
            # every token changes string state
            inString = not inString
            
            # handle empty tokens (i.e. two successive double quotation marks (") 
            # or a quotation mark as the last character in src    
            if len(tok.strip()) == 0:
                if not inString:
                    quote.append('"')
                    if inQuote:
                        self.buffer.append("".join(quote))
                        quote = []
                    inQuote = not inQuote
                    continue


            if inQuote:
                quote.append(tok.strip())
            elif inString :
                self.buffer = self.buffer + tok.split()
            else:
                if len(self.buffer) != 0:
                    self.newTree.append(" ".join(self.buffer))
                    self.buffer = []
                    countComplex = countComplex + 1
                    
                countSimple = countSimple + len(tok.split())
                self.newTree = self.newTree + tok.split()

        ## write out any remaining data in buffer
        if len(self.buffer) != 0:
            self.newTree.append(" ".join(self.buffer))
            del self.buffer[:]
            countComplex = countComplex + 1
    
        print "String parsed\n\tsimple values:\t%d\n\tmulti word values:\t%d"\
            % (countSimple, countComplex)
        return self.newTree

