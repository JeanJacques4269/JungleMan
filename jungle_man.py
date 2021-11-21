import pygame.math

from constants import *


class Jungleman(pygame.sprite.Sprite):
    def __init__(self, spawn):
        super().__init__()
        self.img_right = img_jungleman
        self.img_left = pygame.transform.flip(img_jungleman, True, False)
        self.VEL = 400
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)
        self.pos = vec(*spawn) * block_size
        self.direction = "right"
        self.surface = self.img_right
        self.rect = self.surface.get_rect()

    def update_position(self, platforms):
        """Fonction where we take care of physics"""
        self.acc = vec(0, 1)  # gravity
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        hits = self.colision(platforms)
        # check wether to go on top of the thing you collided with
        if self.vel.y > 0 and hits and self.pos.y - 5 <= hits[minindex(hits)].rect.bottom:
            self.vel.y = 0
            self.pos.y = hits[minindex(hits)].rect.top + 1

    def move(self, info):
        if info == "right":
            self.pos.x += block_size / 8
            self.surface = self.img_right
        elif info == "left":
            self.pos.x -= block_size / 8
            self.surface = self.img_left

        self.direction = info

        if self.pos.x > WIDTH:
            self.pos.x = 0 - char_size[0]
        if self.pos.x < -char_size[0]:
            self.pos.x = WIDTH

    def jump(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and self.pos.y < hits[minindex(hits)].rect.bottom:
            self.vel.y = -20  # jump is exactly 4 blocks

    def colision(self, other):
        return pygame.sprite.spritecollide(self, other, False)

    def die(self, from_what="idk"):
        self.pos = spawn_pos * block_size
        self.vel = vec(0, 0)
        print(from_what)


def minindex(L):
    index, M = 0, L[0].rect.bottom
    for i in range(len(L)):
        if 17 * block_size > L[i].rect.bottom > M:
            index = i
            M = L[i]
    return index
