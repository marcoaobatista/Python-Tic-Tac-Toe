# Python-Tic-Tac-Toe

This is a simple implementation of the classic TicTacToe game in Python. The game is played in the terminal/console.

## Algorithm (main)

1. Create a new game.
2. Display a welcome message.
3. While the user wants to keep playing the game:
   - Restart the game.
   - Display the current board.
   - Check if the game has ended and get the possible winner.
   - While the game has not ended:
     - Handle and get the user input.
     - Make the play.
     - Display the board.
     - Check if the game has ended and get the possible winner.
   - If it was a draw, display the result.
   - Otherwise, display the winner and give them a point.
   - Prompt the user if they want to continue.
4. Display the final scoreboard and a goodbye message.

## Code Explanation

The code defines a `TicTacToe` class that represents the game. It has the following methods:

- `__init__()`: Initializes the game by creating an empty board, setting the current player, and mapping keyboard keys to coordinates in the game board.
- `check_win()`: Checks if any of the players has won or if it was a draw.
- `make_play(key)`: Populates the board with "x" or "o" based on the provided key and changes the current player.
- `display_board()`: Displays the current board.
- `toggle_turn()`: Alternates the turns between "x" and "o".
- `take_input()`: Prompts the user for a key on the board to place "x" or "o" and returns the valid input.
- `display_welcome_message()`: Displays a welcome message and the mapping of keys to board positions.

The `main()` function is the entry point of the program. It creates an instance of the `TicTacToe` class, displays the welcome message, initializes the scoreboard, and starts the game loop. Inside the game loop, it handles user input, makes plays, and checks for a winner or draw. After each game, it updates the scoreboard and asks the user if they want to continue. Finally, it displays the final scoreboard and a goodbye message.

## Usage

To play the TicTacToe game, run the Python script. The game will be displayed in the terminal/console. Follow the instructions to make your moves by entering the corresponding keyboard keys. The game will continue until you choose not to have a rematch.

Have fun playing TicTacToe!
