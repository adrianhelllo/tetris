import config as config_f
import random
import board as board_f
import copy
from config import BOARD_WIDTH, BOARD_HEIGHT

class Tetromino:
    def __init__(self):
        self.shape = random.choice(list(config_f.PIECES.keys()))
        self.cells = config_f.PIECES[self.shape]
        self.position = [0, (BOARD_WIDTH - 1) // 2 - (len(self.cells[0]) - 1) // 2]
        self.cell_positions = self.get_cell_positions(self.cells, self.position)

    def overlay_piece(self, pos, cells, board):
        new_board = copy.deepcopy(board)
        y, x = pos

        for dy, row in enumerate(cells):
            for dx, cell in enumerate(row):
                if cell == 1:
                    new_board[y + dy][x + dx] = 1

        return new_board
    
    def get_cell_positions(self, cells, pos):
        positions = []

        for y in range(len(cells)):
            for x in range(len(cells[0])):
                if cells[y][x] == 1:
                    positions.append([pos[0] + y, pos[1] + x])

        return positions

    def spawn_tetromino(self, board):
        new_board = self.overlay_piece(self.position, self.cells, board)
        self.get_cell_positions(self.cells, self.position)

        return new_board

if __name__ == '__main__':
    tetromino = Tetromino()
    print(tetromino.cells, tetromino.cell_positions)
    tetromino.spawn_tetromino([[0 for _ in range(10)] for _ in range(20)])