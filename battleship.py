from random import randint
"""
=============================================
Codecademy/Learn Python
7 Lists and Functions
  Interactive Lessons: Battleship!
=============================================

Extra Credit: 
  X 1. Make multiple battleships. 
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

    difficulty = {
            "easy" : 30 / 100.0, 
            "medium" : 60 / 100.0, 
            "hard" : 90 / 100.0
            }


    user_difficulty = raw_input("Choose difficulty level(easy, medium, hard): ").lower()

    num_ships = 3
    battleships = []

    
    while len(battleships) != num_ships:
        ship_row = random_row(board)
        ship_col = random_col(board)
        add = ship_row*10 + ship_col

        if not add in battleships:
            battleships.append(add)
            board[ship_row][ship_col] = "G"
        
    
    print_board(board)

    turns_range = int(num_ships/difficulty[user_difficulty])

    for turn in range(turns_range):
        print "turn %d out of %d"%(turn+1, turns_range)
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Coloumn: "))
        add = guess_row*10 + guess_col

        if add in battleships:
            print "Congratulations! You sank a battleship!"
            battleships.remove(add)
            if len(battleships) == 0:
                print "Victory! You sank all my battleships!"
                break
        else:
            if guess_row not in range(len(board)) or guess_col not in range(len(board[0])):
                print "Oops, that's not even in the ocean."
            elif board[guess_row][guess_col] == "X":
                print "You guesses that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                print_board(board)
            if turn+1 == turns_range:
                print "Game Over"




if __name__=="__main__":
    main()
