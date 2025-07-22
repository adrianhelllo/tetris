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

