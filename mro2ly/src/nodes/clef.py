from .node import Node

class Clef(Node):
    CHILDNAMES =  ['shape', 'centre', 'pitchposn']
    SHAPES = ['Treble', 'Bass', 'Alto', 'TrebleUp8', 'TrebleDown8']
    
    def __init__(self, name, value, parent):
        Node.__init__(self, name , value, parent)
