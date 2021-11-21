import pygame
from constants import *
from jungle_man import Jungleman
from level import Platform, generate_platforms
from ennemy import Ennemy
from fruit import Fruit


class Game:
    def __init__(self, win, map):
        self.win = win
        self.character = Jungleman(spawn_pos)
        self.ennemy1 = Ennemy((10 * block_size, 5 * block_size), 10, 13)
        self.fruit = Fruit(fruit_pos)
        self.ground = Platform(32, 0, 18)
        level_platforms = generate_platforms(map)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.character, self.ground, self.ennemy1, self.fruit, *level_platforms)

        self.platforms = pygame.sprite.Group()
        self.platforms.add(self.ground, *level_platforms)

        self.ennemies = pygame.sprite.Group()
        self.ennemies.add(self.ennemy1)

        self.fruits = pygame.sprite.Group()
        self.fruits.add(self.fruit)

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
                    self.character.jump(self.platforms)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.character.move("left")
            if keys[pygame.K_RIGHT]:
                self.character.move("right")

            self.updated_positions()
            self.check_win_death()
            self.draw_everything()

    def check_win_death(self):
        if self.character.colision(self.ennemies):
            print("die")
        if self.character.colision(self.fruits):
            print("win")

    def updated_positions(self):
        self.character.update_position(self.platforms)
        self.ennemy1.update_position()

    def draw_everything(self):
        for entity in self.all_sprites:
            self.win.blit(entity.surface, entity.rect)
        pygame.display.flip()
