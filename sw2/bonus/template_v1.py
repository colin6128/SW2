# pygame template  - skeleton for a new pygame template
import os
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
yellow = (200, 200, 0)
magenta = (200, 0, 200)
cyan = (0, 200, 200)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
bright_yellow = (255, 255, 0)
bright_magenta = (255, 0, 255)
bright_cyan = (0, 255, 255)

# set up assets folders
# WIndows: "C:\Users\cag\Documents"
# Apple Mac "/Users/cag/Documents"
# Linux "/home/cag/Documents"
game_folder = os.path.dirname(__file__)

# intilise pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# set up sprite group
all_sprites = pygame.sprite.Group()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # Update
    all_sprites.update()
    # Draw / render
    screen.fill(black)
    all_sprites.draw(screen)

    # after drawing everythng, flip the display
    pygame.display.flip()
