import board as board_f
import logic as logic_f
import tetromino as piece_f
import config as config_f

def main():
    playing = True
    board_obj = board_f.Board()
    piece = piece_f.Tetromino()
    board_obj.board = piece.spawn_tetromino(board_obj.board)
    logic_f.update_board(board_obj)

if __name__ == '__main__':
    main()