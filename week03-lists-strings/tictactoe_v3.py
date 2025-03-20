from typing import List, Tuple

def display_board(b: List[List[str]]) -> None:
    for i in range(3):
        print(b[i])

def user_play(b: List[List[str]], p: str) -> Tuple[int, int, bool]:
    print(p, "plays")
    row = int(input("Row (1-3): "))
    col = int(input("Col (1-3): "))
    # Check for valid row and col
    if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid row or/and col")
        return 0, 0, False
    # Check if position row,col is empty
    row -= 1
    col -= 1
    if b[row][col] != '-':
        print("Cell is not empty")
        return 0, 0, False 
    return row, col, True

def update_board(b: List[List[str]], p: str, r: int, c: int) -> None:
    b[r][c] = p

def change_player(p: str) -> str:
    return 'X' if p == 'O' else 'O'

def get_winner(b: List[List[str]]) -> str:
    # Check for winner Rows and Columns
    for i in range(3):
        if b[i][0] == b[i][1] and b[i][0] == b[i][2] and b[i][0] != '-':
            return b[i][0]
        elif b[0][i] == b[1][i] and b[0][i] == b[2][i] and b[0][i] != '-':
            return b[0][i]
    # Check for winner in diagonals 
    if b[0][0] == b[1][1] and b[0][0] == b[2][2] and b[0][0] != '-':
        return b[0][0]
    if b[0][2] == b[1][1] and b[0][2] == b[2][2] and b[0][2] != '-':
        return b[0][2]
    return None

def is_tie(b: List[List[str]]) -> bool:
    t = True
    for i in range(3):
        if '-' in b[i]:
            t = False
            break
    return t


player = 'X'
winner = None
tie = False
board = [['-'] * 3 for i in range(3)]

stop = False

while not stop:
    display_board(board)
    row, col, correct = user_play(board, player)
    if not correct:
        continue 
    update_board(board, player, row, col) 
    player = change_player(player)
    winner = get_winner(board)
    if winner is not None:
        stop = True
        continue 
    if not stop and is_tie(board):
        stop = True
        continue 

display_board()
if winner is not None:
    print("Winner is", winner)
elif tie:
    print("It's a tie")

