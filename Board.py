class Board:
    def __init__(self):
        self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.x_turn = True
        self.draw = False
        self.game_over = False

    def make_move(self, move, undo=False):
        if self.x_turn:
            if not undo:
                self.state[move[0]][move[1]] = 1
            else:
                self.state[move[0]][move[1]] = 0
        else:
            if not undo:
                self.state[move[0]][move[1]] = 2
            else:
                self.state[move[0]][move[1]] = 0
        self.x_turn = not self.x_turn