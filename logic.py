import time
import copy

def update_board(board):
    board.clear_previous()
    board.render_board()

def shift_active_piece(board, piece):
    shifted_board = copy.deepcopy(board)

    if not piece.can_fall(board):
        return False
    
    shifted_board = piece.shift_piece(board)

    return shifted_board

def check_collision():
    pass

