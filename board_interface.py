import json
import time

import board_to_file
from create_board import *
import pygame

# Global Variables
def init_pygame():
    global x,background_color
    background_color = (251, 247, 245)
    pygame.init()
    pygame.display.set_caption("Sudoku Solver")
    x = pygame.display.set_mode((900, 900))  # Surface
    x.fill(background_color)


def get_board():
    board = create_array_board()
    return board


def draw_vertical(adet, d1x, d1y, d2x, d2y):
    # kareler 40 piksel boyutundadır.
    for i in range(0, adet):
        if(i % 3 == 0):
            pygame.draw.line(x, (0, 0, 0),
                             (d1x+40*i, d1y), (d2x+40*i, d2y), 4)
        pygame.draw.line(x, (0, 0, 0),
                         (d1x+40*i, d1y), (d2x+40*i, d2y), 2)


def draw_horizontal(adet, y1x, y1y, y2x, y2y):
    # kareler 40 piksel boyutundadır.
    for i in range(0, adet):
        if(i % 3 == 0):
            pygame.draw.line(x, (0, 0, 0),
                             (y1x, y1y+40*i), (y2x, y2y+40*i), 4)
        pygame.draw.line(x, (0, 0, 0),
                         (y1x, y1y+40*i), (y2x, y2y+40*i), 2)


def draw_square(bo):
    x.fill(background_color)
    board = bo
    # Sol Üst Blok
    draw_vertical(10, 40, 40, 40, 400)
    draw_horizontal(10, 40, 40, 400, 40)

    # Sağ Üst Blok
    draw_vertical(10, 520, 40, 520, 400)
    draw_horizontal(10, 520, 40, 880, 40)

    # Sağ Üst Blok ile Sol Üst Blok Arasındaki 3x3 lük Blok
    draw_vertical(4, 400, 280, 400, 400)
    draw_horizontal(4, 400, 280, 520, 280)

    # Orta Blok
    draw_vertical(10, 280, 400, 280, 520)
    draw_horizontal(4, 280, 400, 640, 400)

    # Sol Alt Blok
    draw_vertical(10, 40, 520, 40, 880)
    draw_horizontal(10, 40, 520, 400, 520)

    # Sağ Alt Blok
    draw_vertical(10, 520, 520, 520, 880)
    draw_horizontal(10, 520, 520, 880, 520)

    # Sol Alt Blok ile Sağ Alt Blok Arasındaki 3x3 lük Blok
    draw_vertical(4, 400, 520, 400, 640)
    draw_horizontal(4, 400, 520, 520, 520)

    # Board değerlerinin ekranda gösterilmesi
    put_numbers(board)

    pygame.display.update()


def put_numbers(bo):
    # Verilen Board Değerleri Ekranda gösterir.
    board = bo
    my_font = pygame.font.SysFont("Comic Sans MS", 35)

    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if(board[i][j] == -1):
                value = my_font.render("", True, (0, 0, 0))
                x.blit(value, ((j+1)*40+13, (i+1)*40+13))
            elif(board[i][j] == "*"):
                value = my_font.render("", True, (0, 0, 0))
                x.blit(value, ((j+1)*40+2, (i+1)*40))
            else:
                value = my_font.render(str(board[i][j]), True, (0, 0, 0))
                x.blit(value, ((j+1)*40+2, (i+1)*40))

    pygame.display.update()


def update_numbers(row, col, num):
    # Verilen Board Değerleri Ekranda gösterir.
    my_font = pygame.font.SysFont("Comic Sans MS", 35)
    # Verilen row ve col değerlerinin olduğu yeri beyaz renge dönüştürür
    x.fill(pygame.Color(251, 247, 245), ((col+1)*40+2, (row+1)*40, 38, 38))
    value = my_font.render("", True, (0, 0, 0))
    x.blit(value, ((col+1)*40+2, (row+1)*40))
    new_value = my_font.render(str(num), True, ("red"))
    x.blit(new_value, ((col+1)*40+2, (row+1)*40))
def update():
    pygame.display.update()

def wait():
    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
    except:
        pass

# if __name__ == "__main__":
#
#     board = get_board()
#     draw_square(board)
#     update_numbers(1, 4, 9)
#     """    for i in board_to_json.get_steps_in_db():
#         draw_square(json.loads(i[1]))
#         time.sleep(2)
#     """
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
