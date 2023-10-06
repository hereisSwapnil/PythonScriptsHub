import random
from sudoku_lp import SudokuSolver

class SudokuBoardGenerator:
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]
        self.solver = SudokuSolver(self.board)

    def fill_board(self):
        for i in range(0, 9, 3):
            nums = random.sample(range(1, 10), 9)
            k = 0
            for j in range(i, i + 3):
                self.board[j][i:i + 3] = nums[k:k + 3]
                k += 3
        self.solver.solve()

    def remove_numbers(self, count):
        for _ in range(count):
            row, col = random.randint(0, 8), random.randint(0, 8)
            while self.board[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            self.board[row][col] = 0

    def get_board(self):
        return [row[:] for row in self.board]


