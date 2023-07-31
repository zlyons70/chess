from copy import deepcopy
import pygame
# validmoves key is the piece, value is a list of valid moves
def negaMax (position, depth, maxPlayer, game):
    if depth == 0 or game.checkmate() or game.stalemate():
        return game.evaluate(), position
    max = float('-inf')
    for move in getAllMoves(position, maxPlayer, game):
        score = -negaMax(move, depth -1, -maxPlayer, game)
        if score > max:
            max = score
    return max

def getAllMoves(board, maxPlayer, game):
    moves = []
    validMoves = game.validMoves
    for piece in validMoves.keys():
        for move in validMoves[piece]:
            tempBoard = deepcopy(board)
            #tempGame = deepcopy(game)
            newstate = simulateMove(tempBoard, game, piece, move)
            moves.append([newstate, piece])
    return moves

def simulateMove(board, game, piece, move):
    game.selectedPiece = piece
    game._move(move)
    return game
# def maxi (postion, depth, maxPlayer, game):
#     if depth == 0 or game.checkmate() or game.stalemate():
#         return game.evaluate(), position
#     max = float('-inf')
#     for move in game.validMoves:
#         score = mini(move, depth -1, -maxPlayer, game)
#         if score > max:
#             max = score
#     return max

# def min(position, depth, maxPlayer, game):
#     if depth == 0 or game.checkmate() or game.stalemate():
#         return game.evaluate(), position
#     min = float('inf')
#     for move in game.validMoves:
#         score = maxi(move, depth -1, -maxPlayer, game)
#         if score < min:
#             min = score
#     return min