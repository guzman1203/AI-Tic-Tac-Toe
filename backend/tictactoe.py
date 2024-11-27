PLAYER_TOKENS = ['X', 'O']
EMPTY_CELL = " "

class TicTacToe:
    def __init__(self, size:int=3, player_x_first:bool=True):
        """Initialize the game board"""
        self.size = size
        self.board = [[EMPTY_CELL for j in range(size)] for i in range(size)]
        self.current_player = PLAYER_TOKENS[0] if player_x_first else PLAYER_TOKENS[1]
        self.game_over = False
        self.turnNumber = 0
    
    def get_board(self) -> list[list[str]]:
        """Return the game board"""
        return self.board
    
    def display_console_board(self) -> None:
        """Display the board in the console"""
        print()
        print("-"*(4*self.size+1))
        for i in range(self.size):
            console_line = "| "
            for j in range(self.size):
                console_line += self.board[i][j] + " | "
            print(console_line)
            print("-"*(4*self.size+1))    

    def _switch_turns(self) -> None:
        """Switch turns"""
        self.current_player = PLAYER_TOKENS[0] if self.current_player == PLAYER_TOKENS[1] else PLAYER_TOKENS[1]

    def _is_valid_move(self, r:int, c:int) -> bool:
        if not (0 <= r < self.size) or not (0 <= c < self.size) or self.board[r][c] != EMPTY_CELL:
            return False
        return True 
    
    def make_move(self, r:int, c:int) -> bool:
        """Make a move"""
        if self._is_valid_move(r,c):
            self.board[r][c] = self.current_player
            self._switch_turns()
            return True
        return False
    
    def _check_winner(self) -> bool:
        for i in range(self.size):
            if all(self.board[i][j] == self.current_player for j in range(self.size)): # Row
                return True
            
            if all(self.board[j][i] == self.current_player for j in range(self.size)):
                return True
        if (all(self.board[i][i] == self.current_player for i in range(self.size)) or
            all(self.board[i][self.size - 1 - i] == self.current_player for i in range(self.size))):
            return True
        return False
    
    def _check_draw(self) -> bool:
        return all(self.board[row][col] != EMPTY_CELL for row in range(self.size) for col in range(self.size))
        
    def play_console_game(self):
        game_won, game_draw = False, False
        while not self.game_over:
            self.display_console_board()
            row = int(input(f"Player {self.current_player}, enter row (0-{self.size-1}): "))
            col = int(input(f"Player {self.current_player}, enter col (0-{self.size-1}): "))
            if self.make_move(row,col):        
                self.turnNumber += 1
                if self.turnNumber >= self.size:
                    if self._check_winner():
                        self.display_console_board()
                        self.game_over=True
                        print(f"Congratulations player {self.current_player}, YOU'VE WON!")
                    elif self._check_draw():
                        self.display_console_board()
                        self.game_over=True
                        print(f"Unlucky! Game has drawn.")
            else:
                print("Invalid move. Please try again!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_console_game()

            