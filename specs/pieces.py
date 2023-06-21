import pygame

class Piece:
    Empty = 0
    King = 1
    Pawn = 2
    Knight = 3
    Bishop = 4
    Rook = 5
    Queen = 6
    
    White = 8
    Black = 16

    boardToFen = {
        Empty : '.',
        King | White : 'K',
        King | Black : 'k',
        Pawn | White : 'P',
        Pawn | Black : 'p',
        Knight | White : 'N',
        Knight | Black : 'n',
        Bishop | White : 'B',
        Bishop | Black : 'b',
        Rook | White : 'R',
        Rook | Black : 'r',
        Queen | White : 'Q',
        Queen | Black : 'q'
    }


    bQueen = pygame.image.load('specs/images/bQueen.png')
    wQueen = pygame.image.load('specs/images/wQueen.png')
    bKing = pygame.image.load('specs/images/bKing.png')
    wKing = pygame.image.load('specs/images/wKing.png')
    bPawn = pygame.image.load('specs/images/bPawn.png')
    wPawn = pygame.image.load('specs/images/wPawn.png')
    bBishop = pygame.image.load('specs/images/bBishop.png')
    wBishop = pygame.image.load('specs/images/wBishop.png')
    bKnight = pygame.image.load('specs/images/bKnight.png')
    wKnight = pygame.image.load('specs/images/wKnight.png')
    bRook = pygame.image.load('specs/images/bRook.png')
    wRook = pygame.image.load('specs/images/wRook.png')
    bQueen = pygame.transform.scale(bQueen, (100,100))
    wQueen = pygame.transform.scale(wQueen, (100,100))
    wKing = pygame.transform.scale(wKing, (100,100))
    bKing = pygame.transform.scale(bKing, (100,100))
    bPawn = pygame.transform.scale(bPawn, (100,100))
    wPawn = pygame.transform.scale(wPawn, (100,100))
    bBishop = pygame.transform.scale(bBishop, (100,100))
    wBishop = pygame.transform.scale(wBishop, (100,100))
    bKnight = pygame.transform.scale(bKnight, (100,100))
    wKnight = pygame.transform.scale(wKnight, (100,100))
    bRook = pygame.transform.scale(bRook, (100,100))
    wRook = pygame.transform.scale(wRook, (100,100))