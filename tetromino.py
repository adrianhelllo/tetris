import config as config_f
import random
import board as board_f

class Tetromino:
    def __init__(self, shape=random.choice(list(config_f.PIECES.keys()))):
        self.shape = shape
        self.cells = config_f.PIECES[shape]
        print(self.shape, self.cells)

    def spawn_tetromino(self, board):
        position = [0, (len(board[0])-1)//2-(len(self.cells[0])-1)//2]
        new_board = board
        new_board[position[0]][position[1]] = 1
        return print(new_board)

if __name__ == '__main__':
    tetromino = Tetromino()
    tetromino.spawn_tetromino([[0 for _ in range(10)] for _ in range(20)])