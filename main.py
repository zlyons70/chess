import pygame
from specs.constants import WIDTH, HEIGHT, SQUARE_SIZE
from specs.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    