import time
import random
import keyboard
import board as board_f
import logic as logic_f
import tetromino as piece_f
import config as config_f
from logic import update_render as update
from logic import shift_active_piece as shift
from logic import random_shape as next_s
from config import TICK_RATE as TICK

def main():
    lines_cleared = 0
    next_shape = next_s()
    level = 0
    score = 0

    base_fall_interval = config_f.BASE_FALL_INTERVAL
    soft_drop_interval = config_f.SOFT_DROP_INTERVAL
    playing = True

    board_obj = board_f.Board()
    active_piece = piece_f.Tetromino(next_shape)
    active_piece.spawn_tetromino(board_obj.board)
    update([lines_cleared, next_shape, level, score], board_obj)

    prev_left = False
    prev_right = False
    prev_rot = False
    last_fall_time = time.time()

    while playing:
        now = time.time()
        
        if keyboard.is_pressed(config_f.DOWN_BIND):
            fall_interval = soft_drop_interval
        else:
            fall_interval = base_fall_interval

        if now - last_fall_time >= fall_interval:
            if active_piece.can_fall(board_obj.board):
                active_piece.shift_piece(board_obj.board)
                logic_f.render_with_active(board_obj, active_piece)
            else:
                if logic_f.is_game_over(board_obj.board, board_obj):
                    playing = False
                    break

                board_obj.board = active_piece.overlay_piece(active_piece.position, active_piece.cells, board_obj.board)
                update([lines_cleared, next_shape, level, score], board_obj)

                current_cleared = logic_f.check_line_clears(board_obj)

                if current_cleared:
                    logic_f.do_line_clearing(board_obj, current_cleared)
                    lines_cleared += len(current_cleared)

                if logic_f.is_level_up(lines_cleared):
                    level += 1

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