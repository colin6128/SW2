#! /usr/bin/env python3
"""
Setting up schmup program.

Importing required libraries and setting global variables.
"""
from os import path
import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

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
game_dir = path.dirname(__file__)
img_dir = path.join(game_dir, "img")

# intilise pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    """Creates the player."""

    # sprite for the player
    def __init__(self):
        """Illustrate player.

        Initialises the player and draws them.
        """
        pygame.sprite.Sprite.__init__(self)
        # Simple graphic
        # self.image = pygame.Surface((50, 40))  # simple starting sprite
        # self.image.fill(green)
        # image for graphic
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius = 19
        # pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    # sprite for the enemies - computer controlled sprites
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((30, 40))  # simple starting sprite
        # self.image.fill(red)

        # image for graphic
        # come back and randomly select mob image between meteor and ship
        # self.image = pygame.transform.scale(mob_ship_img, (50, 38))
        self.image = meteor_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        # pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.top > HEIGHT + 10
                or self.rect.left < 25
                or self.rect.right > WIDTH + 20):
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    # sprite for the bullet shot by player
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((10, 20))  # simple starting sprite
        # self.image.fill(yellow)
        self.image = bullet_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if moves off top of the screen
        if self.rect.bottom < 0:
            self.kill()


# Load all game graphics
background = pygame.image.load(path.join(img_dir, "starfield.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "player.png")).convert()
meteor_img = pygame.image.load(path.join(img_dir, "meteorSmall.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserGreen.png")).convert()
mob_ship_img = pygame.image.load(path.join(img_dir, "enemyShip.png")).convert()

# set up sprite group
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()

    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # check to see if a mob hit the player
    #   hits = pygame.sprite.spritecollide(player, mobs,  False)
    hits = (pygame.sprite.spritecollide(
            player, mobs,  False, pygame.sprite.collide_circle))
    if hits:
        running = False

# Draw / render
    screen.fill(black)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    # after drawing ever  ythng, flip the display
    pygame.display.flip()

pygame.quit()
quit()
