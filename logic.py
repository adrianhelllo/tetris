import time
import random
import os
import copy
import config as config_f

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def hex_to_rgb(hex, background=False):
    clear_hex = hex.strip('#')
    return tuple(int(clear_hex[i:i+2], 16) for i in (0, 2, 4))

def style_char(fg_col, bg_col, char):
    fr, fg, fb = hex_to_rgb(fg_col)
    br, bg, bb = hex_to_rgb(bg_col)
    return f'\033[38;2;{fr};{fg};{fb}m\033[48;2;{br};{bg};{bb}m{char}\033[0m'

def luminance(rgb):
    r, g, b = [v / 255 for v in rgb]
    return 0.2126*r + 0.7152*g + 0.0722*b

def contrast_check(fg_hex, bg_hex, threshold=0.4):
    fg_lum = luminance(hex_to_rgb(fg_hex))
    bg_lum = luminance(hex_to_rgb(bg_hex))

    return abs(fg_lum - bg_lum) > threshold

def generate_clr_scheme():
    groups = list(config_f.COLOR_GROUPS)

    fg_group = random.choice(groups)
    bg_group = random.choice(groups)

    fg = random.choice(fg_group)
    bg = random.choice(bg_group)

    while not contrast_check(fg, bg) or fg == bg:
        fg_group = random.choice(groups)
        bg_group = random.choice(groups)

        fg = random.choice(fg_group)
        bg = random.choice(bg_group)

    return fg, bg

def random_shape():
    return random.choice(list(config_f.PIECES.keys()))

def update_render(info, board, fg, bg, filled_l=None):
    lines, next, level, score = info

    clear_terminal()

    render_info(lines, next, level, score, 'top')
    board.render_board(fg, bg, filled_l)
    render_info(lines, next, level, score, 'bottom')

def check_line_clears(board):
    filled_lines = board.check_filled_lines()

    if len(filled_lines) > 0:
        return filled_lines
    
    return 0

def do_line_clearing(board, filled_l):
    time.sleep(0.2)
    board.clear_lines(filled_l)
    board.shift_rest(filled_l)

def get_clear_value(filled_l):
    if len(filled_l) <= 4:
        return config_f.LINE_CLEAR_VALUES[len(filled_l) - 1]
    else:
        return max(config_f.LINE_CLEAR_VALUES)

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

def render_with_active(info, fg, bg, board_obj, active_piece):
    temp_board = active_piece.overlay_piece(active_piece.position, active_piece.cells, board_obj.board)
    original_board = board_obj.board
    board_obj.board = temp_board
    update_render(info, board_obj, fg, bg)
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

def is_level_up(lines_cleared, current_level):
    return lines_cleared >= (current_level + 1) * 10





