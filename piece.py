class Piece:
    def __init__(self, name, color, value, texture=None, teture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.set_texture()
        self.texture_rect = teture_rect
    
class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        super().__init__('Pawn', color, 1.0)
        
class knight(Piece):
    def __init__(self, color):
        super().__init__('Knight', color, 3.0)
        
class Bishop(Piece):
    def __init__(self, color):
        super().__init__('Bishop', color, 3.001)
        
class Rook(Piece):
    def __init__(self, color):
        super().__init__('Rook', color, 5.0)
        
class Queen(Piece):
    def __init__(self, color):
        super().__init__('Queen', color, 9.0)
        
class King(Piece):
    def __init__(self, color):
        super().__init__('King', color, 100.0)
