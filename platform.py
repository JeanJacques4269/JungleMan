import pygame.sprite

from constants import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, length: int, j: int, i: int, height=block_size):
        """
        a Platform object is a pygame sprite with a predifined color and some other characteristics that you can define
        :param length: Number of blocks horizontally
        :param height: Thickness in pixel, if too small, it can cause problems with collision detection
        :param j: j coordinate in the level grid
        :param i: i cooredinate in the level grid
        """
        super().__init__()
        self.length = length
        self.pos = vec(i, j)
        self.surface = pygame.Surface((length * block_size, height))
        self.surface.fill(BROWN)
        self.rect = self.surface.get_rect()
        self.rect.x = j * block_size
        self.rect.y = i * block_size


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
                platforms_to_return.append(Platform(n, a, i, block_size // 2))
            j += 1
    print(len(platforms_to_return))
    return platforms_to_return


