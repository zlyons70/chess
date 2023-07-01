import pygame
from .board import Board
from .pieces import Piece

class Logic:
    
    def pieceType(self, board, piece, position):
        color = piece & Piece.Black
        if color != Piece.Black:
            color = Piece.White

        if piece == Piece.Pawn | Piece.White or piece == Piece.Pawn | Piece.Black:
            return self.pawnLogic(board, position, color)
        if piece == Piece.Rook | Piece.White or piece == Piece.Rook | Piece.Black:
            return self.rookLogic(board, position, color)
        if piece == Piece.Knight | Piece.White or piece == Piece.Knight | Piece.Black:
            return self.knightLogic(board, position, color)
        if piece == Piece.Bishop | Piece.White or piece == Piece.Bishop | Piece.Black:
            return self.bishopLogic(board, position, color)
        if piece == Piece.Queen | Piece.White or piece == Piece.Queen | Piece.Black:
            return self.queenLogic(board, position, color)
        if piece == Piece.King | Piece.White or piece == Piece.King | Piece.Black:
            return self.kingLogic(board, position, color)
    # TODO 
    # I also need to create a function that will check if the king is in check
    
    # Pass each function the board, the piece we want to move, and where the piece is
    # we are then going to return an arry of all valid moves
    # then we will place this array into the dictionary
    # current enpeasant idea, we can keep a variable when a pawn moves 2 spaces, that grabs the position of the pawn that moved two spaces
    # then we can check to see if we have a pawn in position to take this pawn
    # if we don't have a pawn in that position or opt to not take the pawn then we set the variable to None
    
    #TODO En Passant and Promotion
    def pawnLogic(self, board, position, color):
        validMoves = []
        direction = -1
        if color == Piece.Black:
            direction = 1
        if position // 8 == 1 or position // 8 == 6:
            if board[position + 8 * direction] == 0:
                validMoves.append(position + 8 * direction)
                if board[position + 16 * direction] == 0:
                    validMoves.append(position + 16 * direction)
        if board[position + 8 * direction] == 0:
            validMoves.append(position + 8 * direction)
        if position % 8 == 0:
            if color == Piece.White:
                if board[position - 7] & color != color and board[position - 7] != 0:
                    validMoves.append(position - 7)
            else:
                if board[position + 9] & color != color and board[position + 9] != 0:
                    validMoves.append(position + 9)
        elif position % 8 == 7:
            if color == Piece.White:
                if board[position - 9] & color != color and board[position - 9] != 0:
                    validMoves.append(position - 9)
            else:
                if board[position + 7] & color != color and board[position + 7] != 0:
                    validMoves.append(position + 7)
        else:
            if board[position + 7 * direction] & color != color and board[position + 7 * direction] != 0:
                validMoves.append(position + 7 * direction)
            if board[position + 9 * direction] & color != color and board[position + 9 * direction] != 0:
                validMoves.append(position + 9 * direction)
        
        return validMoves
    # 17, 15, -17, -15, +10, -10, +6, -6
    def knightLogic(self, board, position, color):
        validMoves = []
        offsets = [17, 15, -17, -15, 10, -10, 6, -6]
        col = position % 8
        for offset in offsets:
            distance = (position + offset) % 8 - col
            if position + offset >= 0 and position + offset <= 63 and distance <= 2 and distance >= -2:
                if board[position + offset] & color != color:
                    validMoves.append(position + offset)
        return validMoves
    
    def bishopLogic(self, board, position, color):
        validMoves = []
        temp = position + 9
        while temp % 8 <= 7 and temp % 8 > position % 8 and temp <= 63:
            if board[temp] != 0:
                if board[temp] & color == color:
                    break
                else:
                    validMoves.append(temp)
                    break
            validMoves.append(temp)
            temp += 9
        
        temp = position - 9
        while temp % 8 >= 0 and temp % 8 < position % 8 and temp >= 0:
            if board[temp] != 0:
                if board[temp] & color == color:
                    break
                else:
                    validMoves.append(temp)
                    break
            validMoves.append(temp)
            temp -= 9
            
        temp  = position - 7
        while temp % 8 <= 7 and temp % 8 > position % 8 and temp >= 0:
            if board[temp] != 0:
                if board[temp] & color == color:
                    break
                else:
                    validMoves.append(temp)
                    break
            validMoves.append(temp)
            temp -= 7
        
        
        temp = position + 7
        while temp % 8 >= 0 and temp % 8 < position % 8 and temp <= 63:
            if board[temp] != 0:
                if board[temp] & color == color:
                    break
                else:
                    validMoves.append(temp)
                    break
            validMoves.append(temp)
            temp += 7
        return validMoves
    
    def rookLogic(self, board, position, color):
        validMoves = []
        print("In rook logic")
        temp = position + 1
        # right move
        while temp % 8 <= 7 and temp % 8 > position % 8:
            if board[temp] != 0:
                if board[temp] & color == color:
                    break
                else:
                    validMoves.append(temp)
                    break
            validMoves.append(temp)
            temp += 1
        temp = position - 1
        # left move
        while temp % 8 >= 0 and temp % 8 < position % 8:
            if board[temp] != 0:
                if board[temp] & color == color:
                    break
                else:
                    validMoves.append(temp)
                    break
            validMoves.append(temp)
            temp -= 1
        temp = position + 8
        # up move
        while temp <= 63:
            if board[temp] != 0:
                if board[temp] & color == color:
                    break
                else:
                    validMoves.append(temp)
                    break
            validMoves.append(temp)
            temp += 8
        temp = position - 8
        # down move
        while temp >= 0:
            if board[temp] != 0:
                if board[temp] & color == color:
                    break
                else:
                    validMoves.append(temp)
                    break
            validMoves.append(temp)
            temp -= 8
        return validMoves
    
    def queenLogic(self, board, position, color):
        validMoves = []
        validMoves.extend(self.bishopLogic(board, position, color))
        validMoves.extend(self.rookLogic(board, position, color))
        return validMoves
    
    def kingLogic(self, board, position, color):
        validMoves = []
        offset = [-1, 1, -8, 8, -7, 7, -9, 9]
        for move in offset:
            if position + move >= 0 and position + move <= 63:
                if board[position + move] & color != color:
                    validMoves.append(position + move)
                if board[position + move] == 0:
                    validMoves.append(position + move)
                    
        # castling
        if color == Piece.White:
            if board[60] == Piece.White| Piece.King:
                if board[61] == 0 and board[62] == 0 and board[63] == Piece.White| Piece.Rook and board.wKcastle == True:
                    validMoves.append(62)
            if board[60] == Piece.White| Piece.King and board.wQcastle == True:
                if board[59] == 0 and board[58] == 0 and board[57] == 0 and board[56] == Piece.White| Piece.Rook:
                    validMoves.append(58)
        if color == Piece.Black:
            if board[4] == Piece.Black| Piece.King:
                if board[5] == 0 and board[6] == 0 and board[7] == Piece.Black| Piece.Rook and board.bKcastle == True:
                    validMoves.append(6)
            if board[4] == Piece.Black| Piece.King and board.bQcastle == True:
                if board[3] == 0 and board[2] == 0 and board[1] == 0 and board[0] == Piece.Black| Piece.Rook:
                    validMoves.append(2)
        
        return validMoves
    
    #def validCastle(self, board, position, color):
        
        
    def checkLogic(self, board, piece, destination):
        return True