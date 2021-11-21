from constants import *


class Fruit(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.surface = img_fruit
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = pos * block_size

