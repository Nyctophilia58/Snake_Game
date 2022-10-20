import pygame
import sys
import random
from pygame.math import Vector2

pygame.init()
cell_size = 40
cell_number = 30


# class Fruit:
#     def __init__(self):
#         self.x = 10
#         self.y = 10
#         self.pos = Vector2(self.x, self.y)
#
#     def draw_fruit(self):
#         fruit_rect = pygame.Rect(self.pos.x, self.pos.y, cell_size, cell_size)
#         pygame.draw.rect(dis, (126, 166, 114), fruit_rect)


dis_width = cell_size * cell_number
dis_height = cell_size * cell_number

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('SNAKE GAME')
icon = pygame.image.load('Pictures/Snake.png')
pygame.display.set_icon(icon)

# fruit = Fruit()

black = (0, 0, 0)
orange = (255, 165, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 102)

snake_block = 10
snake_speed = 10

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("Helvetica", 20)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = font_style.render("Your score: " + str(score), True, red)
    dis.blit(value, [0, 0])


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.ellipse(dis, white, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [dis_width / 2.7, dis_height / 2])


def game_loop():
    x_axis = dis_width / 2
    y_axis = dis_height / 2

    x_axis_change = 0
    y_axis_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, dis_width - snake_block)/10.0)*10.0
    food_y = round(random.randrange(0, dis_height - snake_block)/10.0)*10.0
    count = 1

    game_over = False
    game_close = False

    while not game_over:
        # while game_close:
        #     dis.fill(black)
        #     message("You Lost! Press Q-Quit or C-Play Again", green)
        #     pygame.display.update()
        #
        #     for event in pygame.event.get():
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_q:
        #                 game_over = True
        #                 game_close = False
        #             if event.key == pygame.K_c:
        #                 game_loop()

        while game_close:
            dis.fill(black)
            message("""You Lost! Do you want to play again? (y/n)""", green)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        game_loop()
                    elif event.key == pygame.K_q:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_axis_change = -snake_block
                    y_axis_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_axis_change = snake_block
                    y_axis_change = 0
                elif event.key == pygame.K_UP:
                    y_axis_change = -snake_block
                    x_axis_change = 0
                elif event.key == pygame.K_DOWN:
                    y_axis_change = snake_block
                    x_axis_change = 0

        if x_axis >= dis_width or x_axis < 0 or y_axis >= dis_height or y_axis < 0:
            game_close = True

        x_axis += x_axis_change
        y_axis += y_axis_change
        dis.fill(black)
        pygame.draw.rect(dis, orange, [food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(x_axis)
        snake_head.append(y_axis)

        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # fruit.draw_fruit()

        if x_axis == food_x and y_axis == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            count += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()


game_loop()
