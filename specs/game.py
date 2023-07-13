import pygame
from pygame.locals import *
from .board import Board
from .pieces import Piece
from .logic import Logic
# This file is responsible for the game logic
# This is good because we don't clutter main
# TODO
# en passant
# pawn promotion
# turn counter
# 50 move rule
# Fix white square bishop bug
class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    # This function updates our board
    def update(self):
        self.board.drawSquares(self.win)
        self.board.createBoard(self.win)
        if self.highlightMoves == True:
            self.board.drawValidMoves(self.win, self.validMoves[self.selectedPiece])
        pygame.display.update()
            
        #self.selectedPiece = None
    # This function will be used to determine the state of the game after
    # each move, we need to check for checkmate, stalemate, etc.
    # TODO
    # Make helper functions for each of these
    # 50 move rule.
    # cannot castle out of check
    def beginNewTurn(self):
        if self.turn == Piece.White:
            self.turn = Piece.Black
            self.board.blackCheck = not self.logic.checkLogic(self.board.board, self.board.blackKingPosition, Piece.Black)
            self.board.halfMoves = 1
        else:
            self.turn = Piece.White
            self.board.whiteCheck = not self.logic.checkLogic(self.board.board, self.board.whiteKingPosition, Piece.White)
            self.board.fullMoves += 1
            self.board.halfMoves = 0
        if self.board.whiteCheck == True or self.board.blackCheck == True:
            self.checkmate()
        self.stalemate()
        if self.board.halfMoves == 50:
            print("Draw by 50 move rule")
        if self.board.threeFold == True:
            print("Draw by 3 fold repetition")
        return
            
    def _init(self):
        self.selectedPiece = None
        self.board = Board()
        self.turn = Piece.White
        self.validMoves = {}
        self.logic = Logic()
        self.highlightMoves = False
    
    def reset(self):
        self._init()

    def select(self, pos):
        destination = None
        self.highlightMoves = False
        currentKingPos = self.board.whiteKingPosition if self.turn == Piece.White else self.board.blackKingPosition
        if self.selectedPiece is None or self.board.board[self.selectedPiece] == 0:
            print("in Select first conditional")
            print(self.board.board[pos])
            if self.board.board[pos] != 0 and self.board.board[pos] & self.turn == self.turn:
                self.selectedPiece = pos
                piece = self.board.board[self.selectedPiece]
                if self.validMoves.get(self.selectedPiece) == None:
                    print("generating move on click")
                    self.validMoves[self.selectedPiece] = self.logic.pieceType(self.board.board, piece, self.selectedPiece, self.board, currentKingPos)
                print(self.validMoves[self.selectedPiece])
                if piece < 16 and self.turn == Piece.Black:
                    self.highlightMoves = False
                elif piece > 16 and self.turn == Piece.White:
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
                print("In en passant conditional")
                print("Destination", destination)
                self.board.enPassant = destination
            if self.board.enPassant != -1:
                if destination == self.board.enPassant + (8 * direction):
                    self.board.board[self.board.enPassant] = 0
            if destination <= 7 or destination >= 56:
                self.pawnPromotion()
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
        self.beginNewTurn()
    
    def moveValid(self, destination):
        piece = self.board.board[self.selectedPiece]
        print("In Move Valid pre if", self.turn, "piece", piece)
        if piece < 16 and self.turn == Piece.Black:
            return False
        if piece > 16 and self.turn == Piece.White:
            return False
        print("Selected piece ", self.selectedPiece)
        if destination in self.validMoves[self.selectedPiece]:
            self.validMoves = {}
            return True
        print("Invalid Move")
        return False
    
    def generateAllValidMoves(self):
        print("In generate all valid moves")
        if self.turn == Piece.White:
            currentKingPos = self.board.whiteKingPosition
        else:
            currentKingPos = self.board.blackKingPosition
        for i in range(63):
            if self.board.board[i] != 0 and self.board.board[i] & self.turn == self.turn:
                print("Board Position ", i)
                piece = self.board.board[i]
                self.validMoves[i] = self.logic.pieceType(self.board.board, piece, i, self.board, currentKingPos)
                print(piece)
                print(self.validMoves[i])
                
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
                print("Checkmate")
        if self.board.blackCheck == True:
            print("Black is in check")
            total = self.generateAllValidMoves()
            if total == 0:
                print("Checkmate")
        return
    
    def stalemate(self):
        if self.board.whiteCheck == False and self.board.blackCheck == False:
            total = self.generateAllValidMoves()
            if total == 0:
                print("Stalemate")
        return
    
    def pawnPromotion(self):
        return