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
    score = 0
    fall_interval = TICK * 20
    playing = True

    board_obj = board_f.Board()
    active_piece = piece_f.Tetromino()
    active_piece.spawn_tetromino(board_obj.board)
    update(board_obj)

    prev_left = False
    prev_right = False
    prev_rot = False
    last_fall_time = time.time()

    while playing:
        now = time.time()

        if now - last_fall_time >= fall_interval:
            if active_piece.can_fall(board_obj.board):
                active_piece.shift_piece(board_obj.board)
                logic_f.render_with_active(board_obj, active_piece)
            else:
                if logic_f.is_game_over(board_obj.board, board_obj):
                    playing = False
                    break

                board_obj.board = active_piece.overlay_piece(active_piece.position, active_piece.cells, board_obj.board)
                update(board_obj)

                logic_f.check_line_clears(board_obj)

                active_piece = piece_f.Tetromino()
                active_piece.spawn_tetromino(board_obj.board)

            last_fall_time = now

        cur_left = keyboard.is_pressed(config_f.LEFT_BIND)
        cur_right = keyboard.is_pressed(config_f.RIGHT_BIND)
        cur_rot = keyboard.is_pressed(config_f.ROTATE_BIND)

        if cur_left and not prev_left:
            active_piece.move_horizontally(board_obj.board, config_f.LEFT_BIND)

        if cur_right and not prev_right:
            active_piece.move_horizontally(board_obj.board, config_f.RIGHT_BIND)

        if cur_rot and not prev_rot:
            active_piece.rotate_piece(board_obj.board)

        logic_f.render_with_active(board_obj, active_piece)

        prev_left = cur_left
        prev_right = cur_right
        prev_rot = cur_rot
        
        time.sleep(TICK)

if __name__ == '__main__':
    main()