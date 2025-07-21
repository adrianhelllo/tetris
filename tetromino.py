import config as config_f
import random
import board as board_f
import copy

class Tetromino:
    def __init__(self):
        self.shape = random.choice(list(config_f.PIECES.keys()))
        self.cells = config_f.PIECES[self.shape]

    def overlay_piece(self, pos, cells, board):
        new_board = copy.deepcopy(board)
        y, x = pos

        for dy, row in enumerate(cells):
            for dx, cell in enumerate(row):
                if cell == 1:
                    new_board[y + dy][x + dx] = 1

        return new_board

    def spawn_tetromino(self, board):
        position = [0, (len(board[0]) - 1) // 2 - (len(self.cells[0]) -1 ) // 2]
        new_board = self.overlay_piece(position, self.cells, board)

        return new_board

if __name__ == '__main__':
    tetromino = Tetromino()
    tetromino.spawn_tetromino([[0 for _ in range(10)] for _ in range(20)])