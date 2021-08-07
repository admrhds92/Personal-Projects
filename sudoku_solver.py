board = [
    [7, 8, "_", 4, "_", "_", 1, 2, "_"],
    [6, "_", "_", "_", 7, 5, "_", "_", 9],
    ["_", "_", "_", 6, "_", 1, "_", 7, 8],
    ["_", "_", 7, "_", 4, "_", 2, 6, "_"],
    ["_", "_", 1, "_", 5, "_", 9, 3, "_"],
    [9, "_", 4, "_", 6, "_", "_", "_", 5],
    ["_", 7, "_", 3, "_", "_", "_", 1, 2],
    [1, 2, "_", "_", "_", 7, 4, "_", "_"],
    ["_", 4, 9, 2, "_", 6, "_", "_", 7]
]


def solve(board):
    find = find_empty(board)
    if not find:  # BASE CASE --- If we cant find an empty spot then the board is solved
        print("\nSolution:")
        print_board(board)
        return True
    else:
        row, col = find  # The empty spot is assigned

    for i in range(1, 10):
        if isValid(board, i, (row, col)):
            # If spot is valid place the current number from the loop
            board[row][col] = i

            if solve(board):  # Recursive call until base case is reached
                return True

            board[row][col] = '_'


# Checks if placement of num is valid
def isValid(board, num, pos):
    # Check Row
    for i in range(len(board[0])):
        # checks every row to not be a number already in that row
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Col
    for i in range(len(board[0])):
        # checks every col to not be a number already in that row
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check Box 1 - 9 of sudoku board
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    # Move is valid
    return True


def print_board(theBoard):

    boardSize = len(theBoard)
    rowSize = len(theBoard[0])

    # Print horizontal grid line every 3 lines
    for i in range(boardSize):
        if i % 3 == 0 and i != 0:
            print("------------------------")

    # Print vertical grid lines every 3 lines
        for j in range(rowSize):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

    # Print the numbers and blanks of the board
            if j == 8:
                print(theBoard[i][j])  # Print element with newline
            else:
                # Print without newline
                print(str(theBoard[i][j]) + " ", end="")


def find_empty(theBoard):
    boardSize = len(theBoard)
    rowSize = len(theBoard[0])

    for i in range(boardSize):
        for j in range(rowSize):
            if theBoard[i][j] == "_":
                return (i, j)  # row, col

    # No blanks found
    return None


print_board(board)
solve(board)
# print_board(board)
