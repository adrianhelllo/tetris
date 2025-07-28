import time
import os
import copy
import config as config_f

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def update_board(board, filled_l=None):
    clear_terminal()
    board.render_board(filled_l)

def check_line_clears(board):
    filled_lines = board.check_filled_lines()

    if len(filled_lines) > 0:
        update_board(board, filled_lines)
        time.sleep(0.15)
        board.clear_lines(filled_lines)
        board.shift_rest(filled_lines)

        return len(filled_lines)
    
    return 0

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

def render_with_active(board_obj, active_piece):
    temp_board = active_piece.overlay_piece(active_piece.position, active_piece.cells, board_obj.board)
    original_board = board_obj.board
    board_obj.board = temp_board
    update_board(board_obj)
    board_obj.board = original_board

def render_info(lines, next, level, score, side):
    if side == 'top':
        short_range = (0, 2)
    elif side == 'bottom':
        short_range = (2, 4)

    shorthands = [config_f.BOTTOM_INFO_SHORTHANDS[i] for i in range(*short_range)]
    args = [lines, next, level, score]

    info_pairs = list(zip(shorthands, args))

    for pair in info_pairs:
        print(f"{pair[0]}: {pair[1]}", end=' | ')
    print()

def is_level_up(lines_cleared):
    if lines_cleared == 0:
        return False
    return lines_cleared % 10 == 0



