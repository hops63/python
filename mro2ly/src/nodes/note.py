from .node import Node

class Note(Node):
    CHILDNAMES =  ['shape', 'staveoffset', 'p', 'accid', 'accid_dc', 'normalside']
    SHAPES = ['Breve', 'Sbreve', 'Minim', 'Solid', 'Breverest', 'Sbreverest', 
              'Minimrest', 'Crotchetrest', 'Quaverrest', 'Squaverrest', 'DSquaverrest', 
              'HDSquaverrest', 'MultiBarRest']
    ACCIDENTALS = ['None', 'Sharp', 'Flat', 'Natural', 'DoubleSharp', 'DoubleFlat', 
                   'NaturalSharp', 'NaturalFlat']
        
    def __init__(self, name, value, parent):
        Node.__init__(self, name, value, parent)