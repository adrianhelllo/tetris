import board as board_f
import logic as logic_f
import tetromino as piece_f
import config as config_f

def main():
    playing = True
    board_obj = board_f.Board()
    board_obj.board[1][3] = 1
    print(board_obj.board[0][5], "hi")
    logic_f.update_board(board_obj)

if __name__ == '__main__':
    main()