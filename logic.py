import time
import copy
import config as config_f

def update_board(board, filled_l=None):
    board.clear_previous()
    board.render_board(filled_l)

def check_line_clears(board):
    filled_lines = board.check_filled_lines()

    if len(filled_lines) > 0:
        update_board(board, filled_lines)
        time.sleep(0.15)
        board.clear_lines(filled_lines)
        board.shift_rest(filled_lines)

        return filled_lines

def shift_active_piece(board, piece):
    shifted_board = copy.deepcopy(board)

    if not piece.can_fall(board):
        return False
    
    shifted_board = piece.shift_piece(board)

    return shifted_board

def is_game_over(board, brd_obj):
    message = config_f.GAME_OVER_MESSAGE

    if any(board[0][x] != 0 for x in range(len(board[0]))):
        brd_obj.clear_previous()
        print(message)
        return True
    
    return False

def render_with_active(board_obj, active_piece):
    temp_board = active_piece.overlay_piece(active_piece.position, active_piece.cells, board_obj.board)
    original_board = board_obj.board
    board_obj.board = temp_board
    update_board(board_obj)
    board_obj.board = original_board

def render_info(level, score, lines, next):
    ...

def is_level_up(lines_cleared):
    if lines_cleared == 0:
        return False
    return lines_cleared % 10 == 0



