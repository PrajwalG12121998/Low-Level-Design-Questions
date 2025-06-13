from board import Board

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = player1

    def play(self):
        self.board.print_board()
        while not self.board.is_full() and not self.board.has_winner():
            print(f"{self.current_player.get_player_name()}'s turn.")
            
            row = self.get_valid_input("Enter row between 0-2")
            col = self.get_valid_input("Enter column between 0-2")
            try:
                self.board.make_move(row, col, self.current_player.get_player_symbol())
                self.board.print_board()
                self.switch_player()
            except ValueError as e:
                print(str(e))



    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
    
    def get_valid_input(self, message):
        while True:
            try:
                input_val = int(input(message))
                if 0 <= input_val <= 2:
                    return input_val
                else:
                    print("Invalid input! Please type anything between 0-2 both inclusive")
            except ValueError:
                print("Print anything in between 0 and 2 both inclusive")