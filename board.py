import os
import time
from config import BOARD_WIDTH, BOARD_HEIGHT

class Board:
    def __init__(self, width=BOARD_WIDTH, height=BOARD_HEIGHT):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]

    def clear_previous(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def check_filled_lines(self, board):
        filled_indices = []
        for y in range(len(board)):
            if all(cell == 1 for cell in board[y]):
                filled_indices.append(y)

    def flash_cleared_lines(self, filled):
        ...
        
    def shift_rest(self):
        ...

    def clear_lines(self, filled_l, board):
        for line_y in filled_l:
            board[line_y] = [0] * len(board[line_y])

    def render_board(self):
        print('=' * BOARD_WIDTH * 2)
        for row in self.board:
            for cell in row:
                if cell == 0:
                    print(".", end=' ')
                else:
                    print("■", end=' ')
            print('|')
        print('=' * BOARD_WIDTH * 2)

    

if __name__ == '__main__':
    pass

