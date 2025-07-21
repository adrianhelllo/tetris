import time
import board as board_f
import logic as logic_f
import tetromino as piece_f
import config as config_f
from logic import update_board as update
from logic import shift_board as shift


def main():
    playing = True
    board_obj = board_f.Board()
    piece = piece_f.Tetromino()
    board_obj.board = piece.spawn_tetromino(board_obj.board)
    update(board_obj)

    for i in range(20):
        time.sleep(0.25)
        board_obj.board = shift(board_obj.board)
        update(board_obj)

        if i % 4 == 0:
            print("creating new tetromino")
            piece = piece_f.Tetromino()

if __name__ == '__main__':
    main()