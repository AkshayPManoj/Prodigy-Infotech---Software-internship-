def is_valid_move(board, row, col, num):
    # Check if the number is already in the row
    if num in board[row]:
        return False
    
    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the number is already in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    row, col = find_empty_location(board)
    if row is None and col is None:
        return True
    
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    
    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def input_puzzle():
    print("Enter the Sudoku puzzle row by row, use '0' to represent empty cells:")
    puzzle = []
    for i in range(9):
        row = input(f"Enter row {i+1} (separate numbers by spaces): ").split()
        row = [int(num) for num in row]
        puzzle.append(row)
    return puzzle

def main():
    # Input Sudoku puzzle
    puzzle = input_puzzle()
    
    if solve_sudoku(puzzle):
        print("Sudoku Solved:")
        print_board(puzzle)
    else:
        print("No solution exists!")

if __name__ == "__main__":
    main()
