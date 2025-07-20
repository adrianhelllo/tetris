import time

def update_board(board):
    board.clear_previous()
    time.sleep(0.25)
    board.render_board()