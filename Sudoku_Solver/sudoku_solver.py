def solve_sudoku(board):
    empty = find_empty_cell(board)
    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid_move(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def is_valid_move(board, num, pos):
    row, col = pos

    if num in board[row]:
        return False

    if num in [board[i][col] for i in range(9)]:
        return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    sudoku_board = [
        [4, 1, 0, 0, 6, 0, 0, 7, 0],
        [0, 0, 3, 0, 8, 5, 0, 0, 9],
        [0, 2, 0, 3, 7, 0, 5, 0, 1],
        [0, 3, 0, 6, 0, 9, 2, 5, 0],
        [6, 0, 0, 5, 0, 1, 0, 0, 0],
        [0, 0, 9, 0, 2, 0, 0, 0, 3],
        [0, 0, 6, 2, 0, 0, 7, 4, 5],
        [0, 0, 0, 4, 0, 6, 8, 0, 0],
        [2, 8, 4, 0, 0, 0, 1, 9, 6],
    ]

    if solve_sudoku(sudoku_board):
        print("Solved Sudoku:")
        print_sudoku(sudoku_board)
    else:
        print("No solution exists.")
