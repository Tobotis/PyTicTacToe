import time
import random


def get_value(board):
    if board.draw:
        return 0
    elif board.game_over and board.x_turn:
        return float("-inf")
    elif board.game_over and not board.x_turn:
        return float("inf")
    else:
        return 0


def find_best_move(board):
    global position_counter
    position_counter = 0
    time.sleep(0.4)
    move = find_min_max_alpha_beta(board.get_moves(), board, float("-inf"), float("inf"), is_first=True)
    return move


def find_random_move(moves, delay=0):
    time.sleep(delay)
    if len(moves) > 0:
        return moves[random.randint(0, len(moves) - 1)]
    return None


def find_min_max_alpha_beta(moves, board, a,b, is_first=False):
    global position_counter, best_move
    if is_first:
        best_move = find_random_move(moves)

    position_counter += 1
    if board.draw or board.game_over:
        value = get_value(board)
        if is_first:
            return best_move
        return value
    elif board.x_turn:
        max_eval = float("-inf")
        for move in moves:
            board.make_move(move)
            evaluation = find_min_max_alpha_beta(board.get_moves(), board, a, b)
            if evaluation > max_eval:
                max_eval = evaluation
                if is_first:
                    best_move = move
            board.make_move(move, undo=True)
            a = max(a, evaluation)
            if b <= a:
                break
        if is_first:
            print(str(best_move) + " with score of " + max_eval)
            return best_move
        return max_eval
    else:
        min_eval = float("inf")
        for move in moves:
            board.make_move(move)
            evaluation = find_min_max_alpha_beta(board.get_moves(), board, a, b)
            if evaluation < min_eval:
                min_eval = evaluation
                if is_first:
                    best_move = move
            board.make_move(move, undo=True)
            b = min(b, evaluation)
            if b <= a:
                break
        if is_first:
            print(str(best_move) + " with score of " + min_eval)
            return best_move
        return min_eval
