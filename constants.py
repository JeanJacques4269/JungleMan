from screeninfo import get_monitors
import pygame
from colors import *

main = get_monitors()[0]  # Get screens size
for m in get_monitors()[1:]:
    if m.width > main.width:
        main = m

WIDTH, HEIGHT = int(main.width * 3 / 4), int(main.height * 3 / 4)
FPS = 60

# sprites
background = pygame.transform.scale(pygame.image.load("assets/jungle.jpg"), (WIDTH, HEIGHT))
img_jungleman = pygame.image.load("assets/jungleman.png")
x, y = img_jungleman.get_size()
yp = HEIGHT // 5
xp = x * yp // y
img_jungleman = pygame.transform.scale(img_jungleman, (xp, yp))
down = HEIGHT - yp
# game
ACC = 5
spawn_points = [WIDTH // 10, HEIGHT * 4 // 5]
