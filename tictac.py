class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # 3x3 board
        self.current_winner = None # Keep track of winner!

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Helper method to show board numbers
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check the row, column, and diagonals for a win condition
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False
def play_game():
    tictactoe = TicTacToe()
    current_letter = 'X'  # Starting with player X
    tictactoe.print_board_nums()  # Print the board with numbers

    while tictactoe.current_winner is None:
        # Get the player's move
        square = int(input(f"{current_letter}'s turn. Input move (0-8): "))
        if tictactoe.make_move(square, current_letter):
            tictactoe.print_board()
            if tictactoe.current_winner:
                print(f"{current_letter} wins!")
                break
            # Alternate between players
            current_letter = 'O' if current_letter == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

        # A simple check for a tie (all spots are taken)
        if ' ' not in tictactoe.board:
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
