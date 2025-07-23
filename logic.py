import time
import copy
import config as config_f

def update_board(board):
    board.clear_previous()
    board.render_board()

def shift_active_piece(board, piece):
    shifted_board = copy.deepcopy(board)

    if not piece.can_fall(board):
        return False
    
    shifted_board = piece.shift_piece(board)

    return shifted_board

def is_game_over(board, brd_obj):
    message = config_f.GAME_OVER_MESSAGE

    if any(board[0][x] == 1 for x in range(len(board[0]))):
        brd_obj.clear_previous()
        print(message)
        return True
    
    return False

