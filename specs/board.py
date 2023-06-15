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
        #self.createBoard()
        
    def drawSquares(self, win):
        win.fill(DARK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, LIGHT, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def createBoard(self, win):
        self.board[0] = Piece.White | Piece.Rook
        
        #print(self.board[0])
        image = pygame.image.load('specs/images/bQueen.png').convert_alpha()
        win.blit(image, (100,100))
        same = self.getImage(image, 100, 100)
        win.blit(same, (0,0))
    
    def getImage(self, sheet, width, height):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0,0), (0,0,width,height))
        image = pygame.transform.scale(image, (100,100))
        image.set_colorkey((255,255,255))
        return image
   # def draw(self, win):
      #  self.draw(win)
      #  for row