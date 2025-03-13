from typing import List

def print_board(b: List[List[str]]) -> None:
    print("TicTacToe Board")
    for row in b:
        for value in row: 
            print(value, end=' ')
        print()

board = [['-'] * 3 for ii in range(3)]

print_board(board)

board[1][1] = 'X'
board[0][2] = 'O'

print_board(board)