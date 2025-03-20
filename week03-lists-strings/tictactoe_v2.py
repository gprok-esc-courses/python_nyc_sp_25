
player = 'X'
winner = None
tie = False
board = [['-'] * 3 for i in range(3)]

stop = False 

while not stop:
    for i in range(3):
        print(board[i])
    print(player, "plays")
    row = int(input("Row (1-3): "))
    col = int(input("Col (1-3): "))
    # Check for valid row and col
    if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid row or/and col")
        continue
    # Check if position row,col is empty
    row -= 1
    col -= 1
    if board[row][col] != '-':
        print("Cell is not empty")
        continue 
    # Everything ok, update board and change player
    board[row][col] = player 
    player = 'X' if player == 'O' else 'O'

    # Check for winner Rows and Columns
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != '-':
            winner = board[i][0]
            stop = True
        elif board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != '-':
            winner = board[0][i]
            stop = True
    # Check for winner in diagonals 
    if not stop and board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != '-':
        winner = board[0][0]
        stop = True
    if not stop and board[0][2] == board[1][1] and board[0][2] == board[2][2] and board[0][2] != '-':
        winner = board[0][2]
        stop = True
    # Check for tie
    if not stop:
        tie = True
        for i in range(3):
            if '-' in board[i]:
                tie = False
        if tie:
            stop = True



for i in range(3):
        print(board[i])
if winner is not None:
    print("Winner is", winner)
elif tie:
    print("It's a tie")