import pygame

class Piece:
    # This representation of the pieces allows us to look at each square in a binary notation
    # 5 bits, three on the right represent piece type 2 on the left are the color of the piece
    Empty = 0
    King = 1
    Pawn = 2
    Knight = 3
    Bishop = 4
    
    White = 8
    Black = 16