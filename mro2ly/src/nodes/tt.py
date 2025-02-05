class Test:
    elements = []
    def __init__(self):
        #self.elements=[]
        pass
            
    def add(self, value):
        self.elements.append(value)
        
    def __len__(self):
        return len(self.elements)
        
        
if __name__ == "__main__":
    t1 = Test()
    t1.add("SCHLUND")	
    t2 = Test()
    
    t1.add('Gier')
    t2.add("blabla")
    
    print len(t1)
    print len(t2)
    print len(Test.elements)
