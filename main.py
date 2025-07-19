import board
import logic
import tetromino
import config

def main():
    playing = True
    board_obj = board.Board()
    logic.update_board(board_obj)


if __name__ == '__main__':
    main()