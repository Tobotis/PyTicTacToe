import pygame as p
import math
from Board import Board

HEIGHT = WIDTH = 500
MAX_FPS = 15
BOARD_SIZE = 3
SQUARE_SIZE = (HEIGHT // BOARD_SIZE) - 10
IMAGES = {}


def load_images():
    IMAGES[1] = p.image.load("images/x.png")
    IMAGES[2] = p.image.load("images/o.png")


def display_board(board, screen):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            surf = p.Surface((SQUARE_SIZE, SQUARE_SIZE))
            surf.fill(p.Color("white"))
            screen.blit(surf, (
                j * (HEIGHT // BOARD_SIZE), i * (HEIGHT // BOARD_SIZE)))
            if board.state[i][j] != 0:
                image = IMAGES[board.state[i][j]]
                image = p.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
                screen.blit(image, p.Rect(j * (HEIGHT // BOARD_SIZE), i * (HEIGHT // BOARD_SIZE), SQUARE_SIZE,
                                          SQUARE_SIZE))


def main():
    p.init()
    p.display.set_caption("TicTacToe")
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    board = Board()

    load_images()

    playing = True
    player1 = True
    player2 = True
    moved = False

    while playing:
        for event in p.event.get():
            if event.type == p.QUIT:
                playing = False
            if not board.game_over and ((player1 and board.x_turn) or (player2 and not board.x_turn)):
                if event.type == p.MOUSEBUTTONDOWN:
                    position = p.mouse.get_pos()
                    c = position[0] // SQUARE_SIZE
                    r = position[1] // SQUARE_SIZE
                    if 0 <= c < BOARD_SIZE and 0 <= r < BOARD_SIZE:
                        if board.state[r][c] == 0:
                            board.make_move((r, c))
        if board.game_over or board.draw:
            print("Game Over")
        display_board(board, screen)
        p.display.flip()
        clock.tick(MAX_FPS)


if __name__ == "__main__":
    main()
    p.quit()
