from values import *
from square import Square


class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for c in range(COLS)]
        self._create()
    
    def _create(self):
        for r in range(ROWS):
            for c in range(COLS):
                self.squares[r][c] = Square(r, c)
            
    def add_piece(self, color):
        pass
