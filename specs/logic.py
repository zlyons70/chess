import pygame
from .board import Board
from .pieces import Piece

class Logic:
    
    def pieceType(self, board, piece, position, boardObject):
        color = piece & Piece.Black
        checkStatus = boardObject.blackCheck
        validMoves = []
        if color != Piece.Black:
            color = Piece.White
            checkStatus = boardObject.whiteCheck
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
            return self.kingLogic(board, position, color, boardObject)
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
    
    def kingLogic(self, board, position, color, boardObj):
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
                if board[61] == 0 and board[62] == 0 and board[63] == Piece.White| Piece.Rook and boardObj.wKCastle == True and self.validCastle(board, "wKCastle") == True:
                    validMoves.append(62)
                if board[59] == 0 and board[58] == 0 and board[57] == 0 and board[56] == Piece.White| Piece.Rook  and boardObj.wQCastle == True and self.validCastle(board, "wQCastle") == True:
                    validMoves.append(58)
        if color == Piece.Black:
            if board[4] == Piece.Black| Piece.King:
                if board[5] == 0 and board[6] == 0 and board[7] == Piece.Black| Piece.Rook and boardObj.bKCastle == True and self.validCastle(board, "bKCastle") == True:
                    validMoves.append(6)
            if board[4] == Piece.Black| Piece.King and boardObj.bQCastle == True and self.validCastle(board, "bQCastle") == True:
                if board[3] == 0 and board[2] == 0 and board[1] == 0 and board[0] == Piece.Black| Piece.Rook:
                    validMoves.append(2)
        
        return validMoves
    
    def validCastle(self, board, castleSide):
        print("In valid castle")
        print(castleSide)
        if castleSide == "wKCastle":
            print("In wKcastle")
            return self.checkLogic(board, 61, Piece.White) and self.checkLogic(board, 62, Piece.White)
        if castleSide == "wQCastle":
            return self.checkLogic(board, 59, Piece.White) and self.checkLogic(board, 58, Piece.White)
        if castleSide == "bKCastle":
            return self.checkLogic(board, 5, Piece.Black) and self.checkLogic(board, 6, Piece.Black)
        if castleSide == "bQCastle":
            return self.checkLogic(board, 3, Piece.Black) and self.checkLogic(board, 2, Piece.Black)
            
        # TODO Need to check to see if any of the squares required for castling are under attack
        # TODO Need to check to see if the king is in check
        # initial idea :
        # I can start at the spots on the board that the king has to pass through to castle and see if these
        # spots can see pieces that would threaten them, using the same logic as what the queen uses to find valid moves
        # if in any of these spots the square can see an enemy piece that spot is not a valid move
        # then using this same logic I can see if the key king spots are under attack
        return
    # This function is going to take a square on the board and it will return whether or not that square is under attack        
    def checkLogic(self, board, position, color):
        # Pawn attack
        print("In check logic")
        if color == Piece.White:
            if position - 9 >= 0 and position - 9 <= 63 and position % 8 != 0:
                if board[position - 9] == Piece.Black| Piece.Pawn:
                    print("Pawn attack 1")
                    return False
            if position - 7 >= 0 and position - 7 <= 63 and position % 8 != 7:
                if board[position - 7] == Piece.Black| Piece.Pawn:
                    print("Pawn attack 2")
                    return False
        if color == Piece.Black:
            if position + 9 >= 0 and position + 9 <= 63 and position % 8 != 7:
                if board[position + 9] == Piece.White| Piece.Pawn:
                    print("Pawn attack 3")
                    return False
                if position + 7 >= 0 and position + 7 <= 63 and position % 8 != 0:
                    if board[position + 7] == Piece.White| Piece.Pawn:
                        print("Pawn attack 4")
                        return False
        # Knight attack
        validMoves = []
        validMoves.extend(self.knightLogic(board, position, color))
        print("Knight Valid Moves: ", validMoves)
        for move in validMoves:
            if board[move] == Piece.Black| Piece.Knight and color == Piece.White:
                print("Knight attack 1")
                return False
            if board[move] == Piece.White| Piece.Knight and color == Piece.Black:
                print("Knight attack 2")
                return False
        # Bishop attack
        validMoves = []
        validMoves.extend(self.bishopLogic(board, position, color))
        for move in validMoves:
            if board[move] == Piece.Black| Piece.Bishop and color == Piece.White or board[move] == Piece.Black| Piece.Queen and color == Piece.White:
                print("Bishop attack 1")
                return False
            if board[move] == Piece.White| Piece.Bishop and color == Piece.Black or board[move] == Piece.White| Piece.Queen and color == Piece.Black:
                print("Bishop attack 2")
                return False
        validMoves = []
        validMoves.extend(self.rookLogic(board, position, color))
        for move in validMoves:
            if board[move] == Piece.Black| Piece.Rook and color == Piece.White or board[move] == Piece.Black| Piece.Queen and color == Piece.White:
                print("Rook attack 1")
                return False
            if board[move] == Piece.White| Piece.Rook and color == Piece.Black or board[move] == Piece.White| Piece.Queen and color == Piece.Black:
                print("Rook attack 2")
                return False
        print("checkLogic failed")
        return True
    
    def notInCheck(self, validMoves, board, checkStatus, position):
        temp = board
        while checkStatus == True:
            for move in validMoves:
                return