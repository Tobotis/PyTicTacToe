import pygame as p


HEIGHT = WIDTH = 512
MAX_FPS = 15
SQUARE_SIZE = 100
IMAGES = {}

def load_images():
    IMAGES[1] = p.image.load("images/cross.png")
    IMAGES[2] = p.image.load("images/circle.png")


def display_board(board):

