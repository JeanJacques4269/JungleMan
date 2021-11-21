from constants import *


class Ennemy(pygame.sprite.Sprite):
    def __init__(self, pos, start: int, end: int):
        super().__init__()
        self.surface = img_sausage
        self.rect = self.surface.get_rect()
        self.direction = "right"
        self.default_speed = 1
        self.vel = vec(self.default_speed * block_size / FPS, 0)
        self.pos = vec(pos) * block_size
        self.start, self.end = start, end

    def update_position(self):
        self.pos += self.vel if self.direction == "right" else (-1 * self.vel)
        if self.pos.x + char_size.x > (self.end + 1) * block_size:
            self.direction = "left"
            self.pos.x = (self.end + 1) * block_size - char_size.x
        elif self.pos.x < self.start * block_size:
            self.direction = "right"
            self.pos.x = self.start * block_size

        self.rect.bottomleft = self.pos
