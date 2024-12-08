def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Check if the current player has won."""
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    
    return False

def is_board_full(board):
    """Check if the board is completely filled."""
    return all(cell != " " for row in board for cell in row)

def play_tic_tac_toe():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Players
    players = ["X", "O"]
    current_player = 0
    
    while True:
        # Print the current board
        print_board(board)
        
        # Current player's turn
        player = players[current_player]
        print(f"Player {player}'s turn")
        
        # Get player move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                
                # Validate move
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter valid numbers.")
        
        # Check for winner
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = (current_player + 1) % 2

# Start the game
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    play_tic_tac_toe()
