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

    def check_filled_lines(self):
        filled_indices = []
        for y in range(len(self.board)):
            if all(cell == 1 for cell in self.board[y]):
                filled_indices.append(y)

        self.clear_lines(filled_indices)
        return filled_indices

    def shift_rest(self):
        ...

    def clear_lines(self, filled_l):
        for line_y in filled_l:
            self.board[line_y] = [0] * len(self.board[line_y])

    def render_board(self, filled_l):
        print('=' * BOARD_WIDTH * 2)
        for y in range(len(self.board)):
            for x in self.board[y]:
                if y in filled_l:
                    print("▒", end=' ')
                elif x == 0:
                    print(".", end=' ')
                else:
                    print("■", end=' ')
            print('|')
        print('=' * self.width * 2)


    

if __name__ == '__main__':
    pass

