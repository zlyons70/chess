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
    # TODO
    # notes for later, I think that I need to have a function that see's whether or not I'm selecting a piece
    # or if i'm selecting a square to move to
    # once I have this figured out I can then move the seleced piece to the selected square
    # after this function gets working, I can then start working on the logic for the pieces
    def select(self, pos):
        destination = None
        self.highlightMoves = False
        if self.selectedPiece is None or self.board.board[self.selectedPiece] == 0:
            print("in Select first conditional")
            print(self.board.board[pos])
            if self.board.board[pos] != 0:
                self.selectedPiece = pos
                piece = self.board.board[self.selectedPiece]
                self.validMoves[self.selectedPiece] = self.logic.pieceType(self.board.board, piece, self.selectedPiece)
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
        piece = self.selectedPiece
        if piece == self.turn & Piece.King:
            if self.turn == Piece.White:
                self.board.wKCastle = False
                self.board.wQCastle = False
            else:
                self.board.bKCastle = False
                self.board.bQCastle = False
        self.board.move(piece, destination)
        self.selectedPiece = None
        self.turn = Piece.Black if self.turn == Piece.White else Piece.White
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
            