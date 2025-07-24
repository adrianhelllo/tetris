import time
import keyboard
import board as board_f
import logic as logic_f
import tetromino as piece_f
import config as config_f
from logic import update_board as update
from logic import shift_active_piece as shift
from config import TICK_RATE as TICK

def main():
    fall_interval = 4
    playing = True
    left_pressed = False
    right_pressed = False

    board_obj = board_f.Board()
    active_piece = piece_f.Tetromino()

    active_piece.spawn_tetromino(board_obj.board)
    update(board_obj)

    while playing:
        for i in range(fall_interval):
            if keyboard.is_pressed(config_f.LEFT_BIND):
                if not left_pressed:
                    print("Left key pressed")
                    left_pressed = True
                else:
                    left_pressed = False

            if keyboard.is_pressed(config_f.RIGHT_BIND):
                if not right_pressed:
                    print("Right key pressed")
                    right_pressed = True
                else:
                    right_pressed = False

            time.sleep(TICK)
            if i % fall_interval == 0:
                if active_piece.can_fall(board_obj.board):
                    active_piece.shift_piece(board_obj.board)
                    temp_board = active_piece.overlay_piece(active_piece.position, active_piece.cells, board_obj.board)
                    original_board = board_obj.board
                    board_obj.board = temp_board
                    update(board_obj)
                    board_obj.board = original_board
                else:
                    if logic_f.is_game_over(board_obj.board, board_obj):
                        playing = False
                        break

                    board_obj.board = active_piece.overlay_piece(active_piece.position, active_piece.cells, board_obj.board)
                    update(board_obj)
                    active_piece = piece_f.Tetromino()
                    active_piece.spawn_tetromino(board_obj.board)

if __name__ == '__main__':
    main()