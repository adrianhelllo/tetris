import time
import logic as logic_f
import config as config_f
from config import BOARD_WIDTH, BOARD_HEIGHT

class Board:
    def __init__(self, width=BOARD_WIDTH, height=BOARD_HEIGHT):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]

    def check_filled_lines(self):
        filled_indices = []
        for y in range(len(self.board)):
            if all(cell != 0 for cell in self.board[y]):
                filled_indices.append(y)

        return filled_indices

    def shift_rest(self, filled_l):
        shifted_board = [row for i, row in enumerate(self.board) if i not in filled_l]

        num_l_cleared = len(filled_l)
        for _ in range(num_l_cleared):
            shifted_board.insert(0, [0] * self.width)

        self.board = shifted_board

    def clear_lines(self, filled_l):
        for line_y in filled_l:
            self.board[line_y] = [0] * len(self.board[line_y])

    def render_board(self, fg, bg, filled_l=None):
        print('=' * BOARD_WIDTH * 2)
        for y in range(len(self.board)):
            for x in self.board[y]:
                if filled_l and y in filled_l:
                    print(config_f.LINE_CLEAR_CHAR, end=' ')
                elif x == 0:
                    print(config_f.BOARD_LINING_CHAR, end=' ')
                else:
                    print(logic_f.style_char(fg, bg, config_f.CELL_FILL_CHAR), end=' ')
            print('|')
        print('=' * self.width * 2)
        

if __name__ == '__main__':
    pass

