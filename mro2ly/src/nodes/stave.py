from .node import NodeWithList
from .nodelist import NodeList
from .bar import Bar
from .lyrics import LyricLine, Text, Dynamic

class Stave(NodeWithList):
    """Pesentation of a single staff"""
    CHILDNAMES =  ['top', 'left', 'width', 'size', 'voicessplit', 'joinedtobelow', 'stavelink', 'bars', 'lyriclines']

    def __init__(self, name, value, parent):
        NodeWithList.__init__(self, name, value, parent, 
            [("bars", Bar), ("lyriclines", LyricLine), 
            ("texts", Text), ("dynamics", Dynamic)])

            