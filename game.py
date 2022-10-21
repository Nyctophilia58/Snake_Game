import pygame
import sys
import random
from pygame.math import Vector2
import time


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 30
cell_number = 30
scr_width = cell_size * cell_number
scr_height = cell_size * cell_number
screen = pygame.display.set_mode((scr_width, scr_height))
background = pygame.image.load('Pictures/background.png')
clock = pygame.time.Clock()


def button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pygame.font.SysFont("Arial", size)
    text_render = font.render(text, True, fg)
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, bg, (x, y, w, h))
    return screen.blit(text_render, (x, y))


def start():
    print("Ok, let's go")


def hover(button):
    if button.collidepoint(pygame.mouse.get_pos()):
        button = button(screen, (300, 300), "Quit me", 50, "red on green")
    else:
        button = button(screen, (300, 300), "Quit me", 50, "red on yellow")


def welcome_page():
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    message("***WELCOME TO MY SNAKE GAME***", purple, [100, dis_height / 3 - 100])
    pygame.display.update()


def menu():
    welcome_page()
    b0 = button(dis, (150, dis_height/3), "NEW GAME", 50, "purple on green")
    b1 = button(dis, (150, dis_height/3+50), "LOAD GAME", 50, "purple on green")
    b2 = button(dis, (150, dis_height/3+100), "OPTIONS", 50, "purple on green")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if b0.collidepoint(pygame.mouse.get_pos()):
                    b0 = button(dis, (150, dis_height / 3), "NEW GAME", 50, "white on green")
                else:
                    b0 = button(dis, (150, dis_height/3), "NEW GAME", 50, "purple on green")
            if event.type == pygame.MOUSEMOTION:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    b1 = button(dis, (150, dis_height / 3+50), "LOAD GAME", 50, "white on green")
                else:
                    b1 = button(dis, (150, dis_height/3+50), "LOAD GAME", 50, "purple on green")


        pygame.display.update()
    pygame.quit()


menu()
