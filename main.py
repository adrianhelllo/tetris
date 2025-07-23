import time
import board as board_f
import logic as logic_f
import tetromino as piece_f
import config as config_f
from logic import update_board as update
from logic import shift_active_piece as shift


def main():
    playing = True

    board_obj = board_f.Board()
    active_piece = piece_f.Tetromino()

    board_obj.board = active_piece.spawn_tetromino(board_obj.board)

    update(board_obj)

    for i in range(30):
        time.sleep(0.2)
        board_obj.board = shift(board_obj.board, active_piece)
        update(board_obj)

if __name__ == '__main__':
    main()