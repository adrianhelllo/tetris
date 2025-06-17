import os
import time
from config import BOARD_WIDTH, BOARD_HEIGHT

class Board:
    def __init__(self, width=BOARD_WIDTH, height=BOARD_HEIGHT):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]

    def clear_previous():
        os.system('cls' if os.name == 'nt' else 'clear')

    def render_board(self):
        for row in self.board:
            print(row)

board = Board()
board.render_board()

