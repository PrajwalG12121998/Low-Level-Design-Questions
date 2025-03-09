class Board:
    def __init__(self):
        self.grid = [['-' for _ in range(3)] for _ in range(3)]
        self.moves_cnt = 0

    def make_move(self, row, col, symbol):
        if not (0 <= row < 3 and 0 <= col < 3) or self.grid[row][col]!='-':
            raise ValueError("Invalid move!")    
        self.grid[row][col] = symbol
        self.moves_cnt += 1
    
    def is_full(self):
        return self.moves_cnt == 9
    
    def has_winner(self):
        #Check all 3 conditions
        #Check for all rows
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0]!='-':
                return True
        
        for i in range(3):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i]!='-':
                return True

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0]!='-':
            return True

        return self.grid[2][0] == self.grid[1][1] == self.grid[0][2] and self.grid[2][0]!='-'
    
    def print_board(self):
        for i in range(3):
            print(" ".join(self.grid[i]))
        print()

    

