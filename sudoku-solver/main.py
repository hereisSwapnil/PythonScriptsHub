
from generate_board import SudokuBoardGenerator
from sudoku_lp import SudokuSolver
def get_user_board():
    print("Enter your Sudoku board as a 9x9 matrix. Use 0 for empty cells.")
    user_board = []
    for _ in range(9):
        while True:
            try:
                row = list(map(int, input().split()))
                if len(row) != 9 or any(cell < 0 or cell > 9 for cell in row):
                    raise ValueError
                user_board.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter 9 numbers (0-9) separated by spaces.")
    return user_board

def main():
    print("Welcome to the Sudoku Solver!")
    input("Press any key to generate a random Sudoku board or type 'input' to enter your own board: ")

    if input().strip().lower() == 'input':
        sudoku_board = get_user_board()
    else:
        generator = SudokuBoardGenerator()
        generator.fill_board()
        generator.remove_numbers(40)  # Adjust the number as needed
        sudoku_board = generator.get_board()

    print("\nSudoku Board:")
    for row in sudoku_board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

    solver = SudokuSolver(sudoku_board)
    if solver.solve():
        print("\nSolved Sudoku:")
        solver.print_board()
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()