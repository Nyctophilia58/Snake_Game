import pygame
import sys
import random
from pygame.math import Vector2
import time


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size, cell_number = 30, 30

dis_width, dis_height = cell_size * cell_number, cell_size * cell_number

dis = pygame.display.set_mode((dis_width, dis_height))
background = pygame.image.load('Pictures/background.png')
display_msg_font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()


def button(screen, position, text, size, colors="white"):
    fg = colors
    font = pygame.font.SysFont("Arial", size)
    text_render = font.render(text, True, fg)
    x, y = position
    return screen.blit(text_render, (x, y))


def start():
    print("Ok, let's go")


# def hover(button):
#     if button.collidepoint(pygame.mouse.get_pos()):
#         button = button(dis, (300, 300), "Quit me", 50, "red")
#     else:
#         button = button(dis, (300, 300), "Quit me", 50, "red")


def message(msg, color, place):
    msg = display_msg_font.render(msg, True, color)
    dis.blit(msg, place)


def welcome_page():
    dis.fill((0, 0, 0))
    dis.blit(background, (0, 0))
    message("***WELCOME TO MY SNAKE GAME***", (100, 50, 150), [100, dis_height / 3 - 100])
    b0 = button(dis, (150, dis_height/3), "NEW GAME", 30, "purple")
    b1 = button(dis, (150, dis_height/3+50), "LOAD GAME", 30, "purple")
    b2 = button(dis, (150, dis_height/3+100), "OPTIONS", 30, "purple")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if b0.collidepoint(pygame.mouse.get_pos()):
                    b0 = button(dis, (150, dis_height / 3), "NEW GAME", 30, "white")
                else:
                    b0 = button(dis, (150, dis_height/3), "NEW GAME", 30, "purple")
            if event.type == pygame.MOUSEMOTION:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    b1 = button(dis, (150, dis_height / 3+50), "LOAD GAME", 30, "white")
                else:
                    b1 = button(dis, (150, dis_height/3+50), "LOAD GAME", 30, "purple")
        pygame.display.update()


welcome_page()
