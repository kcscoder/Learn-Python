from random import randint
"""
=============================================
Codecademy/Learn Python
7 Lists and Functions
  Battleship!
=============================================

Extra Credit: 
    1. Make multiple battleships. 
    2. Make battleships of different sizes. 
    3. Make your game a two-player game. 
    4. Use functions to allow your game to have more functions
    like rematches, statitstics and more. 

"""

def print_board(board_in):
    """prints the board"""
    for row in board_in:
        print " ".join(row)


def random_row(board_in):
    """gets a random row within range of board"""
    return randint(0, len(board_in)-1)


def random_col(board_in):
    """gets a random column within range of board"""
    return randint(0, len(board_in[0])-1)

def main(): 
    board = []
    for i in range(0,5):
        board.append(["O"]*5)

    ship_row = random_row(board)
    ship_col = random_col(board)
    board[ship_row][ship_col] = "G"
    print_board(board)


    for turn in range(4):
        print "turn: %d"%(turn+1)
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Coloumn: "))

        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sank my battleship!"
            break
        else:
            if guess_row not in range(5) or guess_col not in range(5):
                print "Oops, that's not even in the ocean."
            elif board[guess_row][guess_col] == "X":
                print "You guesses that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                print_board(board)
            if turn == 3:
                print "Game Over"




if __name__=="__main__":
    main()
