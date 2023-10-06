from sudoku_lp import SudokuSolver
from generate_board import SudokuBoardGenerator



# Example usage:
generator = SudokuBoardGenerator()
generator.fill_board()
generator.remove_numbers(40)  # Adjust the number as needed

# Get the generated Sudoku puzzle as a matrix
sudoku_puzzle = generator.get_board()

# Print the puzzle
for row in sudoku_puzzle:
    print(" ".join(str(num) if num != 0 else '0' for num in row))

# Solve the puzzle using your solver
solver = SudokuSolver(sudoku_puzzle)
if solver.solve():
    print("\nSolved Sudoku:")
    solver.print_board()
else:
    print("No solution exists")
