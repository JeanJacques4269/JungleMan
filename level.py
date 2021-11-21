import pygame.sprite
from constants import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, length: int, j: int, i: int):
        """:param length : number of blocks"""
        super().__init__()
        self.length = length
        self.pos = vec(i, j)  # top left
        self.surface = pygame.Surface((length * block_size, block_size))
        self.surface.fill(BROWN)
        self.rect = self.surface.get_rect()
        self.rect.x = j * block_size
        self.rect.y = i * block_size

    def move(self):
        pass


def generate_platforms(L: list):
    platforms_to_return = []
    for i in range(len(L)):
        j = 0
        while j < len(L[0]):
            if L[i][j]:
                a = j
                b = j
                while L[i][j]:
                    b = j
                    j += 1
                n = b - a + 1  # size of the platform
                platforms_to_return.append(Platform(n, a, i))
            j += 1
    print(len(platforms_to_return))
    return platforms_to_return


def beautiful_print(L):
    for a in L:
        print(a)
