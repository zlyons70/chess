import pygame

class Piece:
    # def __init__(self, color, pieceType):
    #     self.color = color
    #     self.pieceType = pieceType
    # This representation of the pieces allows us to look at each square in a binary notation
    # 5 bits, three on the right represent piece type 2 on the left are the color of the piece
    Empty = 0
    King = 1
    Pawn = 2
    Knight = 3
    Bishop = 4
    Rook = 5
    Queen = 6
    
    White = 8
    Black = 16
    
# class Pawn(Piece):
#     def __init__(self, color, pieceType):
#         if color == Piece.White:
#             self.color = Piece.White
#         else:
#             self.color = Piece.Black
#         super().__init__(self, color, pieceType)
#         pawn = color + 2
#         return pawn
        
    
# class Knight(Piece):
#     def __init__(self, color, pieceType):
#         super().__init__(self, color, pieceType)
    
# class Bishop(Piece):
#     def __init__(self, color, pieceType):
#         super().__init__(self, color, pieceType)
        
# class Rook(Piece):
#     def __init__(self, color, pieceType):
#         super().__init__(self, color, pieceType)
        
# class Queen(Piece):
#     def __init__(self, color, pieceType):
#         super().__init__(self, color, pieceType)

# class King(Piece):
#     def __init__(self, color, pieceType):
#         super().__init__(self, color, pieceType)
