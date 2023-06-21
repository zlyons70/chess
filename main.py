import pygame
from specs.constants import WIDTH, HEIGHT, SQUARE_SIZE
from specs.board import Board
from specs.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

def getPositionFromMouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    arrayPosition = row * 8 + col
    return arrayPosition

def main():
    run = True
    # clock makes sure that txhe game runs at a constant FPS
    clock = pygame.time.Clock()
    game = Game(WIN)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # The below is going to check what we've clicked on
            # TODO finish up this function when we're moving pieces
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                arrayPosition = getPositionFromMouse(pos)
                #board.movePiece(arrayPosition)
        game.update()
    pygame.quit()


main()

