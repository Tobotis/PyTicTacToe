class Board:
    def __init__(self):
        self.state = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
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
        self.check_result()

    def check_result(self):
        if self.state[0][0] == self.state[0][1] == self.state[0][2] != 0 or self.state[0][0] == self.state[1][1] == \
                self.state[2][2] != 0 or self.state[0][2] == self.state[1][1] == self.state[2][0] != 0 or self.state[1][
            0] == \
                self.state[1][1] == self.state[1][2] != 0 or self.state[2][0] == self.state[2][1] == self.state[2][
            2] != 0 or \
                self.state[0][0] == self.state[1][0] == self.state[2][0] != 0 or self.state[0][1] == self.state[1][1] == \
                self.state[2][1] != 0 or self.state[0][2] == self.state[1][2] == self.state[2][2] != 0:
            self.game_over = True
        else:
            empty_square = False
            for i in range(len(self.state)):
                for j in range(len(self.state[i])):
                    if self.state[i][j] == 0:
                        empty_square = True
            if empty_square:
                self.game_over = False
                self.draw = False
            else:
                self.draw = True

    def get_moves(self):
        moves = []
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == 0:
                    moves.append((i, j))
        return moves
