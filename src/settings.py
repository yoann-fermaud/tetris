import pygame as pg

vec = pg.math.Vector2

FPS = 59
FIELD_COLOR = (45, 45, 45)
BG_COLOR = (25, 25, 25)

SPRITE_DIR_PATH = "assets/sprites/"
FONT_PATH = "assets/font/Kawai_pixel.TTF"

ANIM_TIME_INTERVAL = 500  # milliseconds
FAST_ANIM_TIME_INTERVAL = 15

TILE_SIZE = 40
FIELD_W, FIELD_H = 15, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_OFFSET_W, FIELD_OFFSET_H = 1.6, 1
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_OFFSET_W, FIELD_RES[1] * FIELD_OFFSET_H


INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.25, FIELD_H * 0.45)
MOVE_DIRECTIONS = {"left": vec(-1, 0), "right": vec(1, 0), "down": vec(0, 1)}

TETROMINOES = {
    "0": [(0, 0), (-1, 0), (1, 0), (0, -1)],
    "1": [(0, 0), (0, -1), (1, 0), (1, -1)],
    "2": [(0, 0), (-1, 0), (0, -1), (0, -2)],
    "3": [(0, 0), (1, 0), (0, -1), (0, -2)],
    "4": [(0, 0), (0, 1), (0, -1), (0, -2)],
    "5": [(0, 0), (-1, 0), (0, -1), (1, -1)],
    "6": [(0, 0), (1, 0), (0, -1), (-1, -1)]
}
