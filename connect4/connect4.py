
class Connect4:
    def __init__(self):
        self.board = []
        self.current_player = None 

    def new_game(self):
        self.current_player = 'R'
        self.board = []
        for r in range(6):
            row = []
            for c in range(7):
                row.append('-')
            self.board.append(row)

    def print_board(self):
        for r in range(6):
            for c in range(7):
                print(self.board[r][c], end=' ')
            print()

    def is_column_full(self, column):
        return self.board[0][column] != '-'
        
    def play(self, column):
        if self.is_column_full(column):
            return False
        else:
            for row in range(6):
                if row == 5 or self.board[row+1][column] != '-':
                    # last row (5) or next row is occupied, so put it here
                    self.board[row][column] = self.current_player
                    self.current_player = 'R' if self.current_player == 'Y' else 'Y'
                    break
            return True
        
    def check_winner(self):
        # check rows
        for row in range(6):
            for col in range(4):
                if self.board[row][col] != '-':
                    if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
                        return self.board[row][col]
        # check columns
        for col in range(7):
            for row in range(3):
                if self.board[row][col] != '-':
                    if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]:
                        return self.board[row][col]
        # check diagonals
        for row in range(3):
            for col in range(3, 7):
                if self.board[row][col] != '-':
                    if self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3]:
                        return self.board[row][col]
        for row in range(3):
            for col in range(4):
                if self.board[row][col] != '-':
                    if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3]:
                        return self.board[row][col]
        return None            
        

if __name__ == '__main__':
    game = Connect4()
    game.new_game()
    while True:
        game.print_board()
        col = int(input(game.current_player + " select column: "))
        if not game.play(col):
            print("Column is full, try again")
        else:
            winner = game.check_winner()
            if winner is not None:
                game.print_board()
                print(winner + " WINS!")
                play_again = input("Play Again? (y/n) ")
                if play_again == 'y':
                    print("===== NEW GAME =====")
                    game.new_game()
                else:
                    print("Bye!")
                    break 
