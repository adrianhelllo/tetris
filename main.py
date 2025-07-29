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
    level = 0
    score = 0

    level_fg, level_bg = logic_f.generate_clr_scheme()

    base_fall_interval = config_f.BASE_DROP_INTERVAL / 60 
    soft_drop_interval = config_f.SOFT_DROP_INTERVAL
    playing = True

    next_shape = next_s()

    board_obj = board_f.Board()
    active_piece = piece_f.Tetromino(next_shape)
    active_piece.spawn_tetromino(board_obj.board)
    next_shape = next_s()
    update([lines_cleared, next_shape, level, score], board_obj, level_fg, level_bg)

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
                logic_f.render_with_active([lines_cleared, next_shape, level, score], level_fg, level_bg, board_obj, active_piece)
                if fall_interval == soft_drop_interval:
                    score += config_f.SOFT_DROP_VALUE
            else:
                if logic_f.is_game_over(board_obj.board, board_obj):
                    playing = False
                    break

                board_obj.board = active_piece.overlay_piece(active_piece.position, active_piece.cells, board_obj.board)

                current_cleared = logic_f.check_line_clears(board_obj)

                update([lines_cleared, next_shape, level, score], board_obj, level_fg, level_bg, current_cleared)

                if current_cleared:
                    logic_f.do_line_clearing(board_obj, current_cleared)
                    lines_cleared += len(current_cleared)
                    score += logic_f.get_clear_value(current_cleared)

                if logic_f.is_level_up(lines_cleared, level):
                    level_fg, level_bg = logic_f.generate_clr_scheme()
                    
                    level += 1

                    if level < 9:
                        base_fall_interval = (config_f.BASE_DROP_INTERVAL - level * 5) / 60
                    else:
                        new_fall_interval = (config_f.FAST_DROP_INTERVAL - (level - 9)) / 60

                        if new_fall_interval * 60 >= 1:
                            base_fall_interval = new_fall_interval
                        else:
                            base_fall_interval = 1 / 60

                active_piece = piece_f.Tetromino(next_shape)
                active_piece.spawn_tetromino(board_obj.board)
                next_shape = next_s()

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

        logic_f.render_with_active([lines_cleared, next_shape, level, score], level_fg, level_bg, board_obj, active_piece)

        prev_left = cur_left
        prev_right = cur_right
        prev_rot = cur_rot
        
        time.sleep(TICK)

if __name__ == '__main__':
    main()