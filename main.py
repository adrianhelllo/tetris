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

    active_piece.spawn_tetromino(board_obj.board)

    update(board_obj)

    for i in range(100):
        time.sleep(0.2)
        if active_piece.can_fall(board_obj.board):
            active_piece.shift_piece(board_obj.board)
            temp_board = active_piece.overlay_piece(active_piece.position, active_piece.cells, board_obj.board)
            original_board = board_obj.board
            board_obj.board = temp_board
            update(board_obj)
            board_obj.board = original_board
        else:
            board_obj.board = active_piece.overlay_piece(active_piece.position, active_piece.cells, board_obj.board)
            update(board_obj)
            active_piece = piece_f.Tetromino()
            active_piece.spawn_tetromino(board_obj.board)

if __name__ == '__main__':
    main()