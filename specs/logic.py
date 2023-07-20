import pygame
from .board import Board
from .pieces import Piece

class Logic:
    
    def pieceType(self, board, piece, position, boardObject, kingPosition):
        color = piece & Piece.Black
        validMoves = []
        invalidMoves = []
        potentialKingMoves = None
        if color != Piece.Black:
            color = Piece.White
        if piece == Piece.Pawn | Piece.White or piece == Piece.Pawn | Piece.Black:
            validMoves = self.pawnLogic(board, position, color, boardObject)
        if piece == Piece.Rook | Piece.White or piece == Piece.Rook | Piece.Black:
            validMoves = self.rookLogic(board, position, color)
        if piece == Piece.Knight | Piece.White or piece == Piece.Knight | Piece.Black:
            validMoves = self.knightLogic(board, position, color)
        if piece == Piece.Bishop | Piece.White or piece == Piece.Bishop | Piece.Black:
            validMoves =  self.bishopLogic(board, position, color)
        if piece == Piece.Queen | Piece.White or piece == Piece.Queen | Piece.Black:
            validMoves =  self.queenLogic(board, position, color)
        if piece == Piece.King | Piece.White or piece == Piece.King | Piece.Black:
            validMoves = self.kingLogic(board, position, color, boardObject)
            potentialKingMoves = validMoves.copy()
        for moves in validMoves:
            if potentialKingMoves != None:
                kingPosition = moves
            tempBoard = board.copy()
            tempBoard[position] = 0
            tempBoard[moves] = piece
            if not self.checkLogic(tempBoard, kingPosition, color):
                invalidMoves.append(moves)
        for moves in invalidMoves:
            validMoves.remove(moves)
        return validMoves

    def pawnLogic(self, board, position, color, boardObject):
        validMoves = []
        direction = -1
        if color == Piece.Black:
            direction = 1
        if position // 8 == 1 or position // 8 == 6:
            if board[position + 8 * direction] == 0:
                validMoves.append(position + 8 * direction)
                temp = position + 16 * direction
                if temp >= 0 and temp <= 63:
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
        if boardObject.enPassant != -1:
            if color == Piece.White:
                temp = position - 9
                if position - boardObject.enPassant == -1:
                    validMoves.append(position - 7)
                else:
                    if position - boardObject.enPassant == 1 and temp % 8 != 7:
                        validMoves.append(position - 9)
            else:
                if position - boardObject.enPassant == 1:
                    validMoves.append(position + 7)
                else:
                    temp = position + 9
                    if position - boardObject.enPassant == - 1 and temp % 8 != 0:
                        validMoves.append(position + 9)
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
        #print("In bishop logic color, ", color)
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
            if position + move >= 0 and position + move <= 63 and abs(position % 8 - (position + move) % 8) <= 1:
                if board[position + move] & color != color:
                    validMoves.append(position + move)
                if board[position + move] == 0:
                    validMoves.append(position + move)
                    
        # castling
        if boardObj != None:
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
        if castleSide == "wKCastle":
            return self.checkLogic(board, 61, Piece.White) and self.checkLogic(board, 62, Piece.White) and self.checkLogic(board, 60, Piece.White)
        if castleSide == "wQCastle":
            return self.checkLogic(board, 59, Piece.White) and self.checkLogic(board, 58, Piece.White) and self.checkLogic(board, 50, Piece.White)
        if castleSide == "bKCastle":
            return self.checkLogic(board, 5, Piece.Black) and self.checkLogic(board, 6, Piece.Black) and self.checkLogic(board, 4, Piece.Black)
        if castleSide == "bQCastle":
            return self.checkLogic(board, 3, Piece.Black) and self.checkLogic(board, 2, Piece.Black) and self.checkLogic(board, 4, Piece.Black)
        return
    # This function is going to take a square on the board and it will return whether or not that square is under attack        
    def checkLogic(self, board, position, color):
        # Pawn attack
        if color == Piece.White:
            if position - 9 >= 0 and position - 9 <= 63 and position % 8 != 0:
                if board[position - 9] == Piece.Black| Piece.Pawn:
                    print("Pawn attack")
                    return False
            if position - 7 >= 0 and position - 7 <= 63 and position % 8 != 7:
                if board[position - 7] == Piece.Black| Piece.Pawn:
                    print("Pawn attack")
                    return False
        if color == Piece.Black:
            if position + 9 >= 0 and position + 9 <= 63 and position % 8 != 7:
                if board[position + 9] == Piece.White| Piece.Pawn:
                    return False
                if position + 7 >= 0 and position + 7 <= 63 and position % 8 != 0:
                    if board[position + 7] == Piece.White| Piece.Pawn:
                        return False
        # Knight attack
        validMoves = []
        validMoves.extend(self.knightLogic(board, position, color))
        for move in validMoves:
            if board[move] == Piece.Black| Piece.Knight and color == Piece.White:
                return False
            if board[move] == Piece.White| Piece.Knight and color == Piece.Black:
                return False
        # Bishop attack
        validMoves = []
        validMoves.extend(self.bishopLogic(board, position, color))
        for move in validMoves:
            if board[move] == Piece.Black| Piece.Bishop and color == Piece.White or board[move] == Piece.Black| Piece.Queen and color == Piece.White:
                return False
            if board[move] == Piece.White| Piece.Bishop and color == Piece.Black or board[move] == Piece.White| Piece.Queen and color == Piece.Black:
                return False
        validMoves = []
        validMoves.extend(self.rookLogic(board, position, color))
        for move in validMoves:
            if board[move] == Piece.Black| Piece.Rook and color == Piece.White or board[move] == Piece.Black| Piece.Queen and color == Piece.White:
                return False
            if board[move] == Piece.White| Piece.Rook and color == Piece.Black or board[move] == Piece.White| Piece.Queen and color == Piece.Black:
                return False
        # King attack
        validMoves = []
        validMoves.extend(self.kingLogic(board, position, color, None))
        for move in validMoves:
            if board[move] == Piece.Black| Piece.King and color == Piece.White:
                return False
            if board[move] == Piece.White| Piece.King and color == Piece.Black:
                return False
        return True