def is_valid(board, row, col, n):
    # Check if the current position is threatened by any queen in the previous rows
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def n_queens_helper(board, row, n):
    if row == n:
        # All queens have been placed
        return True
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row][col] = 1
            if n_queens_helper(board, row+1, n):
                return True
            board[row][col] = 0
    return False

def n_queens(n):
    board = [[0 for j in range(n)] for i in range(n)]
    if n_queens_helper(board, 0, n):
        for row in board:
            print(row)
    else:
        print("No solution found.")

n_queens(4) 
