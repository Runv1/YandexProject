import pygame

from screen import StartScreen, Game
from settings import SIZE

pygame.init()
# pygame.key.set_repeat(200, 70)

screen = pygame.display.set_mode(SIZE)

save = None
while True:
    StartScreen(screen).run()
    Game(screen).run()
