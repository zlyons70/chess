import pygame
from pygame.locals import *
from .board import Board
from .pieces import Piece
from .logic import Logic
class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.selectedPiece = None
        self.board = Board()
        self.validMoves = {}
        self.logic = Logic()
        self.highlightMoves = False
        self.promotionScreen = False
        print(self.board.turn)
        if self.board.turn == 'w':
            self.turn = Piece.White
        else:
            self.turn = Piece.Black
    # This function updates our board and gets the fen value for the turn
    def update(self):
        self.board.drawSquares(self.win)
        self.board.createBoard(self.win)
        if self.highlightMoves == True:
            self.board.drawValidMoves(self.win, self.validMoves[self.selectedPiece])
        if self.promotionScreen == True:
            self.board.drawPromotion(self.win, "Promote Piece: Q, R, B, N")
        pygame.display.update()
        return

    def beginNewTurn(self):
        print("Begin new turn")
        print(self.board.enPassant)
        if self.turn == Piece.White:
            self.turn = Piece.Black
            print("Turn is black")
            self.board.blackCheck = not self.logic.checkLogic(self.board.board, self.board.blackKingPosition, Piece.Black)
            self.board.halfMoves = 1
            if self.board.enPassant // 8 == 3:
                print("En passant is set to -1")
                self.board.enPassant = -1
        else:
            self.turn = Piece.White
            self.board.whiteCheck = not self.logic.checkLogic(self.board.board, self.board.whiteKingPosition, Piece.White)
            self.board.fullMoves += 1
            self.board.halfMoves = 0
            if self.board.enPassant // 8 == 4:
                self.board.enPassant = -1
        if self.board.totalPieces <= 4:
            if self.board.insufficientMaterial():
                self.endGame()
            
        if self.board.whiteCheck == True or self.board.blackCheck == True:
            if self.checkmate():
                self.endGame()
        elif self.stalemate():
            self.endGame()
        elif self.board.fiftyMoveRule == 50:
            print("Draw by 50 move rule")
        elif self.board.threeFold == True:
            print("Draw by 3 fold repetition")
        return
    
    def endGame(self):
        print("Game Over")
        return
    
    def reset(self):
        self._init()

    def select(self, pos):
        destination = None
        self.highlightMoves = False
        currentKingPos = self.board.whiteKingPosition if self.turn == Piece.White else self.board.blackKingPosition
        print(self.board.turn)
        if self.selectedPiece is None or self.board.board[self.selectedPiece] == 0:
            if self.board.board[pos] != 0 and self.board.board[pos] & self.turn == self.turn:
                self.selectedPiece = pos
                piece = self.board.board[self.selectedPiece]
                if self.validMoves.get(self.selectedPiece) == None:
                    self.validMoves[self.selectedPiece] = self.logic.pieceType(self.board.board, piece, self.selectedPiece, self.board, currentKingPos)
                if piece < 16 and self.turn == Piece.Black or piece > 16 and self.turn == Piece.White:
                    self.highlightMoves = False
                else:
                    self.highlightMoves = True
        else:
            destination = pos
            if self.selectedPiece != None and destination != None and self.moveValid(destination): 
                self._move(destination)
            else:
                self.selectedPiece = None
                self.select(pos)


    def _move(self, destination):
        pos = self.selectedPiece
        piece = self.board.board[pos]
        if self.board.enPassant != -1:
            if self.board.board[self.board.enPassant] == Piece.Pawn | self.turn:
                self.board.enPassant = -1
        if piece == Piece.Pawn | self.turn:
            direction = -1 if self.turn == Piece.White else 1
            if abs(pos - destination) == 16:
                self.board.enPassant = destination
            if self.board.enPassant != -1:
                if destination == self.board.enPassant + (8 * direction):
                    self.board.board[self.board.enPassant] = 0
        if piece == Piece.King | self.turn:
            if self.turn == Piece.White:
                print("White king moved")
                self.board.wKCastle = False
                self.board.wQCastle = False
                if pos == 60:
                    if destination == 62:
                        self.board.move(63, 61)
                    elif destination == 58:
                        self.board.move(56, 59)
                self.board.whiteKingPosition = destination
            else:
                self.board.bKCastle = False
                self.board.bQCastle = False
                if pos == 4:
                    if destination == 6:
                        self.board.move(7, 5)
                    elif destination == 2:
                        self.board.move(0, 3)
                self.board.blackKingPosition = destination
        # if the piece we're moving is a rook, we need to disable castling
        if piece == Piece.Rook | self.turn:
            if pos == 0:
                self.board.wQCastle = False
            elif pos == 7:
                self.board.wKCastle = False
            elif pos == 56:
                self.board.bQCastle = False
            elif pos == 63:
                self.board.bKCastle = False
        if self.turn == Piece.White:
            self.board.turn = 'b'
        else: 
            self.board.turn = 'w'
        self.board.move(pos, destination)
        self.selectedPiece = None
        if (destination <= 7 or destination >= 56) and piece == Piece.Pawn | self.turn:
            self.board.board[destination] = self.pawnPromotionPlayer()
            self.board.boardToFen(self.board.board)
        self.beginNewTurn()
    
    def moveValid(self, destination):
        piece = self.board.board[self.selectedPiece]
        if piece < 16 and self.turn == Piece.Black:
            return False
        if piece > 16 and self.turn == Piece.White:
            return False
        if destination in self.validMoves[self.selectedPiece]:
            self.validMoves = {}
            return True
        return False
    
    def generateAllValidMoves(self):
        if self.turn == Piece.White:
            currentKingPos = self.board.whiteKingPosition
        else:
            currentKingPos = self.board.blackKingPosition
        for i in range(63):
            if self.board.board[i] != 0 and self.board.board[i] & self.turn == self.turn:
                piece = self.board.board[i]
                self.validMoves[i] = self.logic.pieceType(self.board.board, piece, i, self.board, currentKingPos)
        total = 0
        for moves in self.validMoves:
            if self.validMoves[moves] == []:
                continue
            else:
                total += len(self.validMoves[moves])
        return total
    
    def checkmate(self):
        if self.board.whiteCheck == True:
            total = self.generateAllValidMoves()
            if total == 0:
                return True
        if self.board.blackCheck == True:
            total = self.generateAllValidMoves()
            if total == 0:
                return True
        return False
    
    def stalemate(self):
        if self.board.whiteCheck == False and self.board.blackCheck == False:
            total = self.generateAllValidMoves()
            if total == 0:
                print("Stalemate")
        return
    
    def pawnPromotionPlayer(self):
        self.promotionScreen = True
        self.update()
        x = 0
        while self.promotionScreen:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        x = Piece.Queen | self.turn
                        self.promotionScreen = False

                    if event.key == pygame.K_r:
                        x = Piece.Rook | self.turn
                        self.promotionScreen = False

                    if event.key == pygame.K_n:
                        x = Piece.Knight | self.turn
                        self.promotionScreen = False

                    if event.key == pygame.K_b:
                        x = Piece.Bishop | self.turn
                        self.promotionScreen = False
        return x