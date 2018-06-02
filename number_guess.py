from random import randint
from time import sleep
"""
Codecademy < Learn Python 
4 Functions
=============================================
Number Guess
=============================================
Asks user to guess a number the computer has 
rolled using two dices.
"""
def get_user_guess():
    guess = int(raw_input("Take a stab at the magic number:"))
    return guess

def roll_dice(number_of_sides):
    first_roll = randint(1,number_of_sides)
    second_roll = randint(1,number_of_sides)
    max_val = number_of_sides * 2

    print "The max value is %d" % max_val

    guess = get_user_guess()

    if guess > max_val or guess < 0:
        print "Sorry, your guess is invalid"
    else:
        print "Rolling..."
        sleep(2)
        print "The first roll is %d" % first_roll
        sleep(1)
        print "The second roll is %d" % second_roll
        sleep(1)

        total_roll = first_roll + second_roll

        print "The total is %d" % total_roll
        print "Result..."

        sleep(1)

        if (guess > total_roll):
            print "You won!"
        else:
            print "You lost!"

def main():
    roll_dice(6)

if __name__=="__main__":
    main()

