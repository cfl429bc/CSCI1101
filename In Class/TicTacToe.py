def generate_board():
    board = [["A","B","C"],
        ["D","E","F"],
        ["G","H","I"]]
    return board

def print_board(board):
    for i,row in enumerate(board):
        for j,col in enumerate(row):
            if j < len(row)-1:
                print(col, end="|")
            else:
                print(col)
        if i < len(board)-1:
            print("-----")
    print()

def do_turn(board, turn):
    print(f"{turn}'s turn!")
    valid = False
    while not valid:
        move = input("Enter move: ")
        if move == "X" or move == "O":
            print("Try again!")
            continue
        for i,row in enumerate(board):
            for j,col in enumerate(row):
                if col == move:
                    board[i][j] = turn
                    valid = True
                    break
            if valid:
                break
        if not valid:
            print("Try again!")

def game_over(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return True
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

def board_full(board):
    for row in board:
        for col in row:
            if col != "X" and col != "O":
                return False
    return True

board = generate_board()
turn = "X"
while True:
    print_board(board)
    do_turn(board, turn)
    if game_over(board):
        print_board(board)
        print(f"{turn} wins!")
        break
    if board_full(board):
        print_board(board)
        print("Draw!")
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"