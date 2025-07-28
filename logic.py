import time
import random
import os
import copy
import config as config_f

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_shape():
    return random.choice(list(config_f.PIECES.keys()))

def update_render(info, board, filled_l=None):
    lines, next, level, score = info

    clear_terminal()

    render_info(lines, next, level, score, 'top')
    board.render_board(filled_l)
    render_info(lines, next, level, score, 'bottom')


def check_line_clears(board):
    filled_lines = board.check_filled_lines()

    if len(filled_lines) > 0:
        return filled_lines
    
    return 0

def do_line_clearing(board, filled_l):
    time.sleep(0.15)
    board.clear_lines(filled_l)
    board.shift_rest(filled_l)

def shift_active_piece(board, piece):
    shifted_board = copy.deepcopy(board)

    if not piece.can_fall(board):
        return False
    
    shifted_board = piece.shift_piece(board)

    return shifted_board

def is_game_over(board, brd_obj):
    message = config_f.GAME_OVER_MESSAGE

    if any(board[0][x] != 0 for x in range(len(board[0]))):
        clear_terminal()
        print(message)
        return True
    
    return False

def render_with_active(info, board_obj, active_piece):
    temp_board = active_piece.overlay_piece(active_piece.position, active_piece.cells, board_obj.board)
    original_board = board_obj.board
    board_obj.board = temp_board
    update_render(info, board_obj)
    board_obj.board = original_board

def render_info(lines, next, level, score, side):
    if side == 'top':
        short_range = (0, 2)
    elif side == 'bottom':
        short_range = (2, 4)

    shorthands = config_f.INFO_SHORTHANDS[short_range[0]:short_range[1]]
    args = [lines, next, level, score][short_range[0]:short_range[1]]

    for stat, value in zip(shorthands, args):
        print(f"{stat}: {value}", end=' | ')
    print()

def is_level_up(lines_cleared):
    if lines_cleared == 0:
        return False
    return lines_cleared % 10 == 0



