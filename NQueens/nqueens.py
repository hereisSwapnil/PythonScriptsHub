def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check if there is a queen in the upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check if there is a queen in the upper-right diagonal
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, row):
        if row == n:
            # If all queens are placed, add the solution to the results
            solutions.append(
                ["".join(["Q" if col == 1 else "." for col in row]) for row in board]
            )
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1  # Place a queen
                solve(board, row + 1)
                board[row][col] = 0  # Backtrack

    solutions = []
    chessboard = [[0] * n for _ in range(n)]
    solve(chessboard, 0)
    return solutions


# Example usage
n = 4
solutions = solve_n_queens(n)
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()
