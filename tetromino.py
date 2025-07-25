import config as config_f
import keyboard
import random
import board as board_f
import copy
import time
from config import BOARD_WIDTH, BOARD_HEIGHT

class Tetromino:
    def __init__(self):
        self.shape = random.choice(list(config_f.PIECES.keys()))
        self.cells = config_f.PIECES[self.shape]
        self.position = [0, (BOARD_WIDTH - 1) // 2 - (len(self.cells[0]) - 1) // 2]
        self.cell_positions = []

    def overlay_piece(self, pos, cells, board):
        new_board = copy.deepcopy(board)
        y, x = pos

        for dy, row in enumerate(cells):
            for dx, cell in enumerate(row):
                if cell != 0:
                    board_y = y + dy
                    board_x = x + dx
                    if 0 <= board_y < len(new_board) and 0 <= board_x < len(new_board[0]):
                        new_board[y + dy][x + dx] = self.shape

        return new_board
    
    def get_cell_positions(self, cells, pos):
        positions = []

        for y in range(len(cells)):
            for x in range(len(cells[0])):
                if cells[y][x] != 0:
                    positions.append([pos[0] + y, pos[1] + x])

        return positions

    def spawn_tetromino(self, board):
        new_board = self.overlay_piece(self.position, self.cells, board)
        self.cell_positions = self.get_cell_positions(self.cells, self.position)

        return new_board
    
    def get_bottom_cells(self, board):
        edge_cells = []
        pos_y, pos_x = self.position

        for x in range(len(self.cells[0])):
            for y in range(len(self.cells) - 1, -1, -1):
                if self.cells[y][x] != 0:
                    board_y = pos_y + y
                    board_x = pos_x + x

                    if board_y + 1 < BOARD_HEIGHT and board[board_y + 1][board_x] == 0:
                        edge_cells.append([board_y, board_x])
                    break
        print(edge_cells)
        return edge_cells
            
    def shift_piece(self, board):
        self.position[0] += 1
        self.cell_positions = self.get_cell_positions(self.cells, self.position)

        return board
    
    def move_horizontally(self, board, direction):
        if direction == config_f.LEFT_BIND:
            self.position[1] -= 1
        elif direction == config_f.RIGHT_BIND:
            self.position[1] += 1

        self.cell_positions = self.get_cell_positions(self.cells, self.position)

    def check_collision(self, board, new_position):
        old_position = self.position
        self.position = new_position
        new_positions = self.get_cell_positions(self.cells, new_position)
        self.position = old_position
        
        if any(x < 0 or x >= len(board[0]) or y < 0 or y >= len(board) for y, x in new_positions):
            return True
        if any(board[y][x] != 0 for y, x in new_positions):
            return True
        return False

    def can_fall(self, board):
        positions = self.get_cell_positions(self.cells, self.position)
        for y, x in positions:
            if y + 1 >= BOARD_HEIGHT:
                return False
            if board[y + 1][x] != 0:
                return False
        return True

if __name__ == '__main__':
    ... #testing