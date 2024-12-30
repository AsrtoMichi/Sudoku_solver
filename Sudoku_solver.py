def solve_sudoku(board):
    empty = next( ((i, j) for i in range(9) for j in range(9) if not board[i][j] ), None)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if not(num in board[row] or
				num in (board[i][col] for i in range(9)) or
				any(board[3 * (row // 3) + i][3 * (col // 3) + j] == num for i in range(3) for j in range(3))):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0

if __name__ == "__main__":
    print("Enter the Sudoku line by line (use 0 for empty cells):")
    board = [list(map(int, input().strip().split())) for _ in range(9)]
    print(f"{chr(10)}Sudoku solved:\n{chr(10).join(' '.join(str(num) for num in row) for row in board)}" if solve_sudoku(board) else "\nNo solution found.")
