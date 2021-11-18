import pygame.math

from constants import *

vec = pygame.math.Vector2


class Jungleman:
    def __init__(self):
        self.img_left = img_jungleman
        self.img_right = pygame.transform.flip(img_jungleman, True, False)
        self.VEL = 400
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)
        self.pos = vec(spawn_points)
        self.direction = "right"

    def update_pos(self):
        self.acc = vec(0, 0.5)
        self.vel += self.acc
        if self.pos.y < down:
            self.pos += self.vel + 0.5 * self.acc
        else:
            self.pos.y = down
            self.vel.y = 0

    def move(self, info):
        if info == "right":
            self.pos.x += self.VEL // FPS * yp // 100
            self.direction = "right"
        elif info == "left":
            self.pos.x -= self.VEL // FPS * yp // 100
            self.direction = "left"

        if info == "jump":
            self.vel.y = -15
            self.pos.y -= 1

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

    def draw(self, win):
        if self.direction == "right":
            img_to_draw = self.img_left
        else:
            img_to_draw = self.img_right
        win.blit(img_to_draw, (self.pos.x, self.pos.y))
