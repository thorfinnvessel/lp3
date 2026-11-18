def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def safe(board, row, col, n):
    for i in range(n):
        if board[i][col] == 1:
            return False

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                if abs(i - row) == abs(j - col):
                    return False

    return True


def solve(board, row, n):
    if row == n:
        return True

    if row == first_row:
        return solve(board, row + 1, n)

    for col in range(n):
        if safe(board, row, col, n):
            board[row][col] = 1

            if solve(board, row + 1, n):
                return True

            board[row][col] = 0

    return False



n = int(input("Enter N: "))

board = [[0 for j in range(n)] for i in range(n)]

first_row = int(input("Enter first queen row (0 to N-1): "))
first_col = int(input("Enter first queen column (0 to N-1): "))

if 0 <= first_row < n and 0 <= first_col < n:
    board[first_row][first_col] = 1

    if solve(board, 0, n):
        print("\nN-Queens Matrix:")
        print_board(board, n)
    else:
        print("Solution does not exist")
else:
    print("Invalid position")