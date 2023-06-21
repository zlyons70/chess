import pygame
from specs.constants import WIDTH, HEIGHT, SQUARE_SIZE
from specs.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

def main():
    run = True
    # clock makes sure that txhe game runs at a constant FPS
    clock = pygame.time.Clock()
    board = Board()
    #game = Game(WIN)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # The below is going to check what we've clicked on
            # TODO finish up this function when we're moving pieces
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.drawSquares(WIN)
        board.createBoard(WIN)
        board.move(board)
        pygame.display.update()
        break
    pygame.quit()


main()

