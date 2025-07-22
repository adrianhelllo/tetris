import time
import board as board_f
import logic as logic_f
import tetromino as piece_f
import config as config_f
from logic import update_board as update
from logic import shift_board as shift


def main():
    playing = True

    pieces = []
    board_obj = board_f.Board()
    pieces.append(piece_f.Tetromino())

    active_piece = pieces[len(pieces) - 1]
    board_obj.board = active_piece.spawn_tetromino(board_obj.board)

    update(board_obj)

    for i in range(30):
        time.sleep(0.2)
        board_obj.board = shift(board_obj.board)
        update(board_obj)

        if i % 10 == 5:
            print("creating new tetromino")
            pieces.append(piece_f.Tetromino())
            active_piece = pieces[len(pieces) - 1]
            board_obj.board =  active_piece.spawn_tetromino(board_obj.board)

if __name__ == '__main__':
    main()