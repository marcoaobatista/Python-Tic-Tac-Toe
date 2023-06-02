"""
############################################################
# TicTacToe Game
#
# Algorithm (main)
#     create new game
#     display welcome message
#     while the user wants to keep playing the game
#         restart game
#         display current board
#         check if game has ended and get the possible winner
#         while the game has not ended
#             handle and get the user input
#             make the play
#             display the board
#             check if game has ended and get the possible winner
#         if it was draw, display it
#         otherwise, display winner and give them a point
#         prompt user if they want to continue
#         change starting player
#     display final scoreboard and goodbye message
############################################################
"""
class TicTacToe(object):
    def __init__(self):
        # Make empty board
        self.board = [[" " for i in range(3)] for j in range(3)]
        # Set current player
        self.turn = "x"
        # Map keyboard keys to coordinates in the game board
        self.hash = {"t":(0,0),"y":(0,1),"u":(0,2),
                     "g":(1,0),"h":(1,1),"j":(1,2),
                     "b":(2,0),"n":(2,1),"m":(2,2)}
    
    
    def check_win(self):
        """ 
        Checks if any of the players won 
        returns: a two item tuple, the first being a bool, true if the game has
ended, and the second item being who won, or if it was a draw
            
        """
        rows = [[],[],[]]
        columns = [[],[],[]]
        diagonals = [[],[]]
        
        uoboard = [] # Unordered board
        
        # Iterate through the board
        for i in range(3):
            for j in range(3):
                # Current board item in the iteration
                cur = self.board[i][j]
                rows[i].append(cur)
                columns[j].append(cur)
                
                # If it is an item in the left right diagonal
                if i-j == 0:
                    diagonals[0].append(cur)
                
                # if it is an item in the right left diagonal
                if abs(i-j) == 2 or (i,j)==(1,1):
                    diagonals[1].append(cur)
                
                uoboard.append(cur)
                
        # Get all rows in the board
        all_rows = rows + columns + diagonals
        
        # Check if either player won
        for lst in all_rows:
            if lst.count("x") == 3:
                return True, "x"
            elif lst.count("o") == 3:
                return True, "o"
            
        # Check if it was a draw
        if uoboard.count("x") + uoboard.count("o") == 9:
            return True, "draw"
        
        return False, ""
    
    
    def make_play(self,key):
        """ Populate board matrix with x or o and changes current player"""
        self.board[self.hash[key][0]][self.hash[key][1]] = self.turn
        self.toggle_turn()
        

    def display_board(self):
        """ Displays current current board """
        print()
        print("{:^3}|{:^3}|{:^3}".format(*self.board[0]))
        print("-"*11)
        print("{:^3}|{:^3}|{:^3}".format(*self.board[1]))
        print("-"*11)
        print("{:^3}|{:^3}|{:^3}".format(*self.board[2]))
        
    
    def toggle_turn(self):
        """ Alternate turns """
        self.turn = "o" if self.turn == "x" else "x"
        

    def take_input(self, cur_player):
        """ 
        Prompts and re-prompts for a key in the board to lay x or o and 
then returns it 
        cur_player: The player that is going to play next
        """
        key = input("Player {}'s ({}) turn: ".format(cur_player, self.turn))
        # Re prompt while it is not a valid key or if place is already filled
        while key not in self.hash or \
                self.board[self.hash[key][0]][self.hash[key][1]] != " ":
            print("\nInvalid key, try again")
            self.display_board()
            key = input("Player {}'s ({}) turn: ".format(cur_player, self.turn))
        return key
                
    
    def display_welcome_message(self):
        """ Displays welcome message and the mapping of the keys """
        print()
        print("=="*34)
        print("xo"*11 + " WELCOME TO TICTACTOE!! " + "xo"*11)
        print("=="*34)
        print()
        print("RULES: Come on, you know how to play this xD")
        print("\tEach position in the board is mapped to your \n\
    keyboard keys as shown below: ")
        print()
        mapped_keys = list(self.hash)
        print("{:^3}|{:^3}|{:^3}".format(*mapped_keys[:3]))
        print("-"*11)
        print("{:^3}|{:^3}|{:^3}".format(*mapped_keys[3:6]))
        print("-"*11)
        print("{:^3}|{:^3}|{:^3}".format(*mapped_keys[6:]))


def opposite_player(player_turn):
    """ Returns player opposite to the input (1 or 2) """
    return 2 if player_turn == 1 else 1

def main():
    game = TicTacToe()
    game.display_welcome_message()
    
    scores = {1:0,2:0}
    cont = "y"
    starting_player = 1
    cur_player = 1
    while cont.lower() == "y":
        print("\n= NEW GAME =")
        game = TicTacToe()
        game.display_board()
        has_ended, winner = game.check_win()
        
        while not has_ended:
            user_input = game.take_input(cur_player)
            game.make_play(user_input)
            game.display_board()
            has_ended, result = game.check_win()
            cur_player = opposite_player(cur_player)
            
        if result == "draw":
            print("\nTHAT'S A DRAW!")
        else:
            print("\n"+result.upper()+" WON. CONGRATULATIONS!")
            if result == "x":
                scores[starting_player] += 1
            else:
                scores[opposite_player(starting_player)] += 1
        
        cont = input("\nDo you want a rematch? (y/n)")
        
        starting_player = opposite_player(starting_player)
    
    if scores[1] == scores[2]:
        print("\nFinal score: {}x{} It's a draw!".format(scores[1], scores[2]))
    else:
        overall_winner = "Player 1" if scores[1] > scores[2] else "Player 2"
        print("\nFinal score: {}x{} for {}"
              .format(scores[1], scores[2], overall_winner))
    
    
    print("- GOODBYEE! -")
    
    
if __name__ == "__main__":
    main()
