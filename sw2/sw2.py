#! /usr/bin/env python3
"""
Setting up program.

Importing required libraries and setting global variables.
"""
import os
import pygame
import random

screen_width = 800
screen_height = 600
FPS = 60
FPS_still = 15

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

block_color = (53, 115, 255)  # colour of things

player_width = 53

pause = False

# set up assets folders
# WIndows: "C:\Users\cag\Documents"
# Apple Mac "/Users/cag/Documents"
# Linux "/home/cag/Documents"
game_folder = os.path.dirname(__file__)

# initialise pygame and create window and associated items
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('A Bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('images/racecar.png')  # car dims 53 x 80 pixels
gameIcon = pygame.image.load('images/racecar_icon.png')
# icon dims 32x32 pixels

# Adding sounds
crash_sound = pygame.mixer.Sound("audio/crash.wav")
pygame.mixer.music.load("audio/Power_Switch.wav")

pygame.display.set_icon(gameIcon)

# In-game text defined
largeText = pygame.font.Font('freesansbold.ttf', 115)
smallText = pygame.font.Font("freesansbold.ttf", 20)


def things_dodged(count):
    """Tracks game score on screen."""
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    screen.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    """Illustrate Mobs."""
    pygame.draw.rect(screen, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    """Illustrate player."""
    screen.blit(carImg, (x, y))


def text_objects(text, font):
    """Illustrate text objects."""
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text, font):
    """Illustrates messages."""
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = ((screen_width / 2), (screen_height / 2))
    # TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(TextSurf, TextRect)


def crash():
    """Game crash screen."""
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    crash = True

    # print(dodged)  # Not workinmsgg as not defined locally

    while crash:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    print("Start Over S key")
                    game_loop()

                if event.key == pygame.K_c:
                    print("Start Over C key")
                    game_loop()

                if event.key == pygame.K_q:
                    quitgame()

                if event.key == pygame.K_e:
                    quitgame()

        message_display("You Crashed", largeText)

        button("Start Over", 150, 450, 150, 50, green, bright_green, game_loop)
        button("End Game", 550, 450, 150, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(FPS_still)


def button(msg, x, y, w, h, ic, ac, action=None):
    """Illustrate functional buttons."""
    mouse = pygame.mouse.get_pos()
    # print(mouse)
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            print(msg + ' button')
            action()

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    # message_display(msg, smallText)
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(TextSurf, TextRect)


def quitgame():
    """Quitting the program."""
    print("quit")
    pygame.quit()
    quit()


def unpause():
    """Unpausing the program."""
    global pause
    pause = False
    pygame.mixer.music.unpause()


def paused():
    """Pausing the program."""
    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    print("Continue key")
                    unpause()

                if event.key == pygame.K_p:
                    print("unPause key")
                    unpause()

                if event.key == pygame.K_q:
                    quitgame()

        # screen.fill(white)
        message_display("Paused", largeText)

        button("Continue", 150, 450, 150, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(FPS_still)


def game_intro():
    """Game Introduction screen."""
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    print("Go! key")
                    game_loop()

                if event.key == pygame.K_s:
                    print("Start! key")
                    game_loop()

                if event.key == pygame.K_q:
                    quitgame()

        screen.fill(white)
        message_display("A Bit Racey", largeText)

        button("Go!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(FPS_still)


def game_loop():
    """Start the game."""
    global pause

    pygame.mixer.music.play(-1)

    x = (screen_width * 0.45)
    y = (screen_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, screen_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    # thing_count = 1

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            #  print(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

                if event.key == pygame.K_p:
                    pause = True
                    print("pause key")
                    paused()

                if event.key == pygame.K_q:
                    quitgame()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        screen.fill(white)

#       things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height,
               block_color)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)
        #  print(dodged)

        if x > screen_width - player_width or x < 0:
            crash()

        if thing_starty > screen_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, screen_width)
            dodged += 1
            thing_speed += 0.2
            thing_width += (dodged * 1.05)

        if y < thing_starty + thing_height:
            # print('ycrossover')

            if (x > thing_startx and
                    x < thing_startx + thing_width
                    or x + player_width > thing_startx and
                    x + player_width < thing_startx + thing_width):
                # print('xcrossover')
                crash()

        pygame.display.flip()
        clock.tick(FPS)


game_intro()
game_loop()
quitgame()
