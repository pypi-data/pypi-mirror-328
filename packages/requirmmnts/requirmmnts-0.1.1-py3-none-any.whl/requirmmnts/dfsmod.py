def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("-" * 20)

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
        
        left_diag = col - (row - i)
        if left_diag >= 0 and board[i][left_diag]:
            return False
        
        right_diag = col + (row - i)
        if right_diag < n and board[i][right_diag]:
            return False
    
    return True

def solve_nqueens(board, row, n, solutions):
    if row == n:
        solutions.append([r[:] for r in board])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n, solutions)
            board[row][col] = 0

def nqueens_dfs(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    
    if solutions:
        print("Solutions Found:")
        for sol in solutions:
            print_board(sol)
    else:
        print("No solution found.")

# Example Usage
n = 8  # Change n for different board sizes
nqueens_dfs(n)