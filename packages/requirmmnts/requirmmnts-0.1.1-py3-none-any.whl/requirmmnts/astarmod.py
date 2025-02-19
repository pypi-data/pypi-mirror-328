import heapq

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

def heuristic(board, n):
    attacks = 0
    queen_positions = [(r, c) for r in range(n) for c in range(n) if board[r][c]]
    
    for i in range(len(queen_positions)):
        for j in range(i + 1, len(queen_positions)):
            r1, c1 = queen_positions[i]
            r2, c2 = queen_positions[j]
            
            if c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                attacks += 1
    
    return attacks

def a_star_nqueens(n):
    pq = []  # Priority queue
    heapq.heappush(pq, (0, 0, [[0] * n for _ in range(n)]))  # (f, g, board)
    
    while pq:
        f, g, board = heapq.heappop(pq)
        row = g  # Next row to place a queen
        
        if row == n:
            print("Solution Found:")
            print_board(board)
            return
        
        for col in range(n):
            if is_safe(board, row, col, n):
                new_board = [r[:] for r in board]
                new_board[row][col] = 1
                h = heuristic(new_board, n)
                heapq.heappush(pq, (g + 1 + h, g + 1, new_board))
    
    print("No solution found.")

# Example Usage
n = 8  # Change n for different board sizes
a_star_nqueens(n)
