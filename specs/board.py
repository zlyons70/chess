import pygame
from .constants import ROWS, COLS, DARK, LIGHT, SQUARE_SIZE
from .pieces import Piece
#from images.Pieces import *
# Create the board object

class Board:
    # here we are def a few attributes of the board class
    def __init__(self):
        self.board = [64]
        self.selectedPiece = None
        self.whitePawns = self.blackPawns = 8
        self.whiteKnights = self.blackKnights = 2
        self.whiteBishops = self.blackBishops = 2
        self.whiteRooks = self.blackRooks = 2
        self.whiteQueens = self.blackQueens = 1
        self.whiteKing = self.blackKing = 1
        self.currentFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        #self.createBoard()
        
    def drawSquares(self, win):
        win.fill(DARK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, LIGHT, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def createBoard(self, win):
        # This is the starting position of the board
        self.fenConvert(self.currentFen, win)
        # We'll need a function that converts from board to fen
        # we can then set currentFen to the output of this function
    
    # This function is used to convert from fen connotation to the board
    def fenConvert(self, fen, win):
        x = 0
        y = 0
        for i in range(len(fen)):
            if fen[i] == '/':
                y += 100
                x = 0
            elif fen[i].isdigit():
                x += (int(fen[i]) * 100)
            else:
                if fen[i] == 'r':
                    self.board.append(Piece.Black | Piece.Rook)
                    win.blit(Piece.bRook, (x,y))
                elif fen[i] == 'n':
                    self.board.append(Piece.Black | Piece.Knight)
                    win.blit(Piece.bKnight, (x,y))
                elif fen[i] == 'b':
                    self.board.append(Piece.Black | Piece.Bishop)
                    win.blit(Piece.bBishop, (x,y))
                elif fen[i] == 'q':
                    self.board.append(Piece.Black | Piece.Queen)
                    win.blit(Piece.bQueen, (x,y))
                elif fen[i] == 'k':
                    self.board.append(Piece.Black | Piece.King)
                    win.blit(Piece.bKing, (x,y))
                elif fen[i] == 'p':
                    self.board.append(Piece.Black | Piece.Pawn)
                    win.blit(Piece.bPawn, (x,y))
                elif fen[i] == 'R':
                    self.board.append(Piece.White | Piece.Rook)
                    win.blit(Piece.wRook, (x,y))
                elif fen[i] == 'N':
                    self.board.append(Piece.White | Piece.Knight)
                    win.blit(Piece.wKnight, (x,y))
                elif fen[i] == 'B':
                    self.board.append(Piece.White | Piece.Bishop)
                    win.blit(Piece.wBishop, (x,y))
                elif fen[i] == 'Q':
                    self.board.append(Piece.White | Piece.Queen)
                    win.blit(Piece.wQueen, (x,y))
                elif fen[i] == 'K':
                    self.board.append(Piece.White | Piece.King)
                    win.blit(Piece.wKing, (x,y))
                elif fen[i] == 'P':
                    self.board.append(Piece.White | Piece.Pawn)
                    win.blit(Piece.wPawn, (x,y))
                x += 100