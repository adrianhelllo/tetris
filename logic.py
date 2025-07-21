import time
import copy

def update_board(board):
    board.clear_previous()
    board.render_board()

def shift_board(board):
    shifted_board = copy.deepcopy(board)

    for y in range(len(shifted_board) - 2, -1, -1):
        for x in range(len(shifted_board[0])):
            if shifted_board[y][x] == 1 and shifted_board[y + 1][x] ==  0:
                shifted_board[y][x], shifted_board[y + 1][x] = 0, 1

    return shifted_board

def check_collision():
    pass

