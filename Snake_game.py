import pygame
import random
import sys
import time
from button import Button

pygame.init()

cell_size = 40
cell_number = 60

dis_width = cell_size * cell_number
dis_height = cell_size * cell_number

SCREEN = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("MENU")
icon = pygame.image.load('Pictures/Snake.png')
pygame.display.set_icon(icon)

black = (0, 0, 0)
orange = (255, 165, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 102)

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("Helvetica", 20)
score_font = pygame.font.SysFont("comicsansms", 35)

dis.fill(green)


def main_menu():
    pygame.display.set_caption("MENU")

    while True:
        dis.blit(white, (0, 0))
        menu_mouse_pos = pygame.mouse.get_pos()

        # menu_text = get_font


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main_menu()
    pygame.display.update()
    clock.tick(10)






