from .tokenizer import Tokenizer


class TreeBuilder:
    """ Converts the content of a MRO file to a list of tuplets.
        The first value of a tuplet is the name of the variable, the second one contains its value.
        This value might be a simple value or a string or again a list of tuplets.
        """

    def parseNodes(self, source):
        tokenizer = Tokenizer()
        tokens = tokenizer.parse(source)
        tree = []
        varname = ""
        parent = [tree]

        for token in tokens:
            if token == "SharpEyeMusicOCROutputFile":
                tree.append((token, ""))
            elif token == "{":
                content = []
                parent[-1].append((varname, content))
                varname = ""
                parent.append(content)
            elif token == "}":
                # close Complex value
                parent.pop()
            else:
                if varname != "":
                    parent[-1].append((varname, token))
                    varname = ""
                else:
                    varname = token
    
        return tree
