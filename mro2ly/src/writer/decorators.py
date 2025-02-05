class PolymorphDecorator(dict):
    """maps types to type specific implementations"""
    def forType(self, type_t):
        """parameterized decorator function. The parameter specifies the 
           class for which the decorated function is valid.
           e.g:  
            @FunctionMap.forType(class)
            def spam(args):
                ...
        """
        def decorated(f):
            def typeTest(*args):
                type_c = args[1].__class__
                try:
                    func = self.__getitem__(type_c)
                    return apply(func, args)
                except KeyError:
                    print("No type specific impl for type %s" % (type_c))
                    raise 
              
            try:
                self.__getitem__(type_t)
                raise Exception("redefining implementation for type %s" % (type_t))
            except KeyError:
                #print("Defining new implementation for type '%s'" % (type_t))
                self.__setitem__(type_t, f)

            return typeTest
        return decorated


