import pygame
from .board import Board
from .pieces import Piece
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
        self.selectedPiece = None
        self.board = Board()
        self.turn = Piece.White
        self.validMoves = {}
        self.win = win
    
    # This function updates our board
    def update(self):
        turn = 0
        self.board.drawSquares(self.win)
        self.board.createBoard(self.win)
        self.board.move(self.board)
        pygame.display.update()