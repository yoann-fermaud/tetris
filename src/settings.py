import pygame as pg

vec = pg.math.Vector2 # We need Vector for the move directions of the blocks and their initial position

FPS = 59
FIELD_COLOR = (45, 45, 45) # FIELD is the right part of the game
BG_COLOR = (25, 25, 25)

# All the paths :
SPRITE_DIR_PATH = "assets/sprites/"
FONT_PATH = "assets/font/Kawai_pixel.TTF"

ANIM_TIME_INTERVAL = 400  # milliseconds
FAST_ANIM_TIME_INTERVAL = 15 # When the user press the down arrow

TILE_SIZE = 40 # All the other poster values will be calculated from the size of the squares
FIELD_W, FIELD_H = 15, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_OFFSET_W, FIELD_OFFSET_H = 1.6, 1
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_OFFSET_W, FIELD_RES[1] * FIELD_OFFSET_H

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0) 
NEXT_POS_OFFSET = vec(FIELD_W * 1.25, FIELD_H * 0.45)
MOVE_DIRECTIONS = {"left": vec(-1, 0), "right": vec(1, 0), "down": vec(0, 1)}

# All the blocks :
TETROMINOES = {
    "0": [(0, 0), (-1, 0), (1, 0), (0, -1)],
    "1": [(0, 0), (0, -1), (1, 0), (1, -1)],
    "2": [(0, 0), (-1, 0), (0, -1), (0, -2)],
    "3": [(0, 0), (1, 0), (0, -1), (0, -2)],
    "4": [(0, 0), (0, 1), (0, -1), (0, -2)],
    "5": [(0, 0), (-1, 0), (0, -1), (1, -1)],
    "6": [(0, 0), (1, 0), (0, -1), (-1, -1)]
}
