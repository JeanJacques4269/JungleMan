import pygame
from constants import *
from game import Game

if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT), )
    game = Game(win, level=1)
    game.run()

