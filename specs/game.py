import pygame
from .board import Board
from .pieces import Piece
from .logic import Logic
# This file is responsible for the game logic
# This is good because we don't clutter main
# TODO
# Who's turn is it?
# Legal moves
# Checkmate
# en passant
# castling
# pawn promotion
# turn counter
# 50 move rule
# 3 fold repetition

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
        currentKing = self.board.whiteKingPosition if self.turn == Piece.White else self.board.blackKingPosition
        if self.selectedPiece is None or self.board.board[self.selectedPiece] == 0:
            print("in Select first conditional")
            print(self.board.board[pos])
            if self.board.board[pos] != 0:
                self.selectedPiece = pos
                piece = self.board.board[self.selectedPiece]
                if self.board.blackCheck == True or self.board.whiteCheck == True:
                    self.generateAllValidMoves()
                else:
                    self.validMoves[self.selectedPiece] = self.logic.pieceType(self.board.board, piece, self.selectedPiece, self.board)
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
        # if castleing move rook
        # if the piece we're moving is the king, we need to disable castling
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
        self.board.move(pos, destination)
        self.selectedPiece = None
        self.turn = Piece.Black if self.turn == Piece.White else Piece.White
        if self.turn == Piece.White:
            self.board.whiteCheck = not self.logic.checkLogic(self.board.board, self.board.whiteKingPosition, self.turn)
        else:
            self.board.blackCheck = not self.logic.checkLogic(self.board.board, self.board.blackKingPosition, self.turn)
        #self.update()
    
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
        for i in range(64):
            if self.board.board[i] != 0 and self.board.board[i] & self.turn == self.turn:
                piece = self.board.board[i]
                testMoves = self.logic.pieceType(self.board.board, piece, i, self.board)
                for j in testMoves:
                    if piece == Piece.King | self.turn:
                            kingPosition = j
                    else:
                        kingPosition = self.board.whiteKingPosition if self.turn == Piece.White else self.board.blackKingPosition
                    temp = self.board.board.copy()
                    print("temp", temp)
                    print("board", self.board.board)
                    temp[i] = 0
                    temp[j] = piece
                    if temp == self.board.board:
                        print("temp == board")
                    if not self.logic.checkLogic(temp, kingPosition, self.turn):
                        testMoves.remove(j)
                self.validMoves[i] = testMoves
        print("Completed generating all valid moves")
        print(self.validMoves)
        return