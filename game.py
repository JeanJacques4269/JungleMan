import pygame
from constants import *
from jungle_man import Jungleman


class Game:
    def __init__(self, win, level):
        self.win = win
        self.level = level
        self.character = Jungleman()

    def run(self):
        game_is_on = True
        clock = pygame.time.Clock()

        while game_is_on:
            clock.tick(FPS)
            self.win.fill(WHITE)
            self.win.blit(background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # si on appuie sur la croix
                    game_is_on = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.character.move("jump")
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.character.move("left")
            if keys[pygame.K_RIGHT]:
                self.character.move("right")
            self.character.update_pos()
            self.draw_everything()

    def draw_everything(self):
        self.character.draw(self.win)
        pygame.display.flip()
