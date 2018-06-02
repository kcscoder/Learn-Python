from random import randint
import time
"""
Codecademy < Learn Python 
5 Lists & Dictionaries
========================================
Rock, Paper, Scissors
========================================
"""

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
        "tie" : "Yawn it's a tie!", 
        "won" : "Yay you won!", 
        "lost" : "Aww you lost!"
        }


def decide_winner(user_choice, computer_choice):
    print "The user chose %s"% user_choice
    time.sleep(1)
    if (user_choice == computer_choice):
        print message["tie"]
    elif (user_choice == "ROCK" and computer_choice == "SCISSORS"):
        print message["won"]
    elif (user_choice == "PAPER" and computer_choice == "ROCK"):
        print message["won"]
    elif (user_choice == "SCISSORS" and computer_choice == "PAPER"):
        print message["won"]
    else:
        print message["lost"]

    time.sleep(1)
    print "The computer chose %s"% computer_choice
    time.sleep(1.3)

def play_RPS():
    user_choice = raw_input("Enter Rock, Paper, or Scissors: ").upper()
    computer_choice = options[randint(0,2)]

    decide_winner(user_choice, computer_choice)


def main():

    print "Let's play Rock, Paper, Scissor!"
    time.sleep(1)
    play_RPS()

if __name__=="__main__":
    main()




