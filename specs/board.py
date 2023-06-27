import pygame
from .constants import ROWS, COLS, DARK, LIGHT, SQUARE_SIZE
from .pieces import Piece
#from .logic import Logic

# Create the board object
class Board:
    # here we are def a few attributes of the board class
    def __init__(self):
        self.board = [0] * 64
        self.selectedPositon = 0
        self.whitePawns = self.blackPawns = 8
        self.whiteKnights = self.blackKnights = 2
        self.whiteBishops = self.blackBishops = 2
        self.whiteRooks = self.blackRooks = 2
        self.whiteQueens = self.blackQueens = 1
        self.whiteKing = self.blackKing = 1
        self.currentFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.halfMoves = 0
        self.fullMoves = 1
        #self.createBoard()
    
    def drawSquares(self, win):
        win.fill(DARK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, LIGHT, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def createBoard(self, win):
        #print(self.board)
        self.fenConvert(self.currentFen, win)
        #print(self.board)
        # TODO
        # We'll need a function that converts from board to fen
        # we can then set currentFen to the output of this function
    
    # This function is used to convert from fen connotation to the board
    def fenConvert(self, fen, win):
        x = 0
        y = 0
        spaceCounter = 0
        boardPosition = 0
        for i in range(len(fen)):
            if spaceCounter > 0:
                if fen[i] == 'w':
                    continue
                    # TODO set turn to white
                elif fen[i] == 'b':
                    continue
                    # TODO set turn to black
                elif fen[i] == 'K':
                    continue
                    # TODO whiteKing castle kingside
                elif fen[i] == 'Q':
                    continue
                    # TODO whiteKing castle queenside
                elif fen[i] == 'k':
                    continue
                    # TODO blackKing castle kingside
                elif fen[i] == 'q':
                    continue
                    # TODO blackKing castle queenside
            elif fen[i] == '/':
                y += 100
                x = 0
            elif fen[i] == ' ':
                spaceCounter += 1
            
            elif fen[i].isdigit():
                x += (int(fen[i]) * 100)
            else:
                boardPosition = int((y/100 * 8) + x/100)
                if fen[i] == 'r':
                    self.board[boardPosition] = Piece.Black | Piece.Rook
                    win.blit(Piece.bRook, (x,y))
                elif fen[i] == 'n':
                    self.board[boardPosition] = Piece.Black | Piece.Knight
                    win.blit(Piece.bKnight, (x,y))
                elif fen[i] == 'b':
                    self.board[boardPosition] = Piece.Black | Piece.Bishop
                    win.blit(Piece.bBishop, (x,y))
                elif fen[i] == 'q':
                    self.board[boardPosition] = Piece.Black | Piece.Queen
                    win.blit(Piece.bQueen, (x,y))
                elif fen[i] == 'k':
                    self.board[boardPosition] = Piece.Black | Piece.King
                    win.blit(Piece.bKing, (x,y))
                elif fen[i] == 'p':
                    self.board[boardPosition] = Piece.Black | Piece.Pawn
                    win.blit(Piece.bPawn, (x,y))
                elif fen[i] == 'R':
                    self.board[boardPosition] = Piece.White | Piece.Rook
                    win.blit(Piece.wRook, (x,y))
                elif fen[i] == 'N':
                    self.board[boardPosition] = Piece.White | Piece.Knight
                    win.blit(Piece.wKnight, (x,y))
                elif fen[i] == 'B':
                    self.board[boardPosition] = Piece.White | Piece.Bishop
                    win.blit(Piece.wBishop, (x,y))
                elif fen[i] == 'Q':
                    self.board[boardPosition] = Piece.White | Piece.Queen
                    win.blit(Piece.wQueen, (x,y))
                elif fen[i] == 'K':
                    self.board[boardPosition]= Piece.White | Piece.King
                    win.blit(Piece.wKing, (x,y))
                elif fen[i] == 'P':
                    self.board[boardPosition] = Piece.White | Piece.Pawn
                    win.blit(Piece.wPawn, (x,y))
                x += 100
    
    def boardToFen(self, board):
        fen = ""
        emptyCounter = 0
        fenMap = Piece.boardToFen
        for i in range(len(self.board)):
            if i % 8 == 0 and i != 0:
                if emptyCounter > 0:
                    fen += str(emptyCounter)
                    emptyCounter = 0
                fen += '/'
            if self.board[i] == 0:
                emptyCounter += 1
            if self.board[i] != 0:
                if emptyCounter > 0:
                    fen += str(emptyCounter)
                    emptyCounter = 0
                fen += fenMap[self.board[i]]
        self.currentFen = fen
        print(fen)
        return fen
 
    def move(self, pos, destination):
        self.selectedPosition = pos
        temp = self.board[self.selectedPosition]
        self.board[self.selectedPosition] = 0
        self.board[destination] = temp
        self.boardToFen(self.board)
        # TODO Decide whether to keep rely on  boardToFen
        #return self.board
    
    def getPiece(self, pos):
        return self.board[pos]
        
        