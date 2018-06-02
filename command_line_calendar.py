"""
Codecademy < Learn Python
8 Loops
===========================================
Command Line Calendar
===========================================
The user should be able to choose to:
    - View the calendar
    - Add an even to the calendar
    - Update an existing event
    - Delete an existing event
The program should behave in the following way:
    + Print a welcome message to the user
    + Prompt the user to view, add, update, or delete an event 
      on the calendar
    + Depending on the user's input: view, add, update, or delete
      an event on the calendar
    + The program should never terminate unless the user decides
      to exit
"""
from time import sleep, strftime


USER_FIRST_NAME = "Bernard"
calendar = {} 

def welcome():
    print "Welcome back, %s" % USER_FIRST_NAME
    print "Your calendar is loading..."
    sleep(1)
    print "Today is: " + strftime("%A %B %d, %Y")
    print "Time is: " + strftime("%H:%M:%S")

    print "What would you like to do?"


def start_calendar():
    welcome()

    start = True
    while start:
        user_choice = raw_input("Type 'A' to Add, 'U' to Update, 'V' to view, 'D' to Delete, 'X' to Exit: ")
        user_choice = user_choice.upper()

        if user_choice == 'V':
            if len(calendar.keys()) < 1:
                print "Currently calendar is empty. "
            else:
     	        print calendar
        elif user_choice == 'U':
            date = raw_input("What date? ")
            update = raw_input("Enter the update: ")
            calendar[date] = update
            print "Update succesful!"
            print calendar
        elif user_choice == 'A':
            event = raw_input("Enter event: ")
            date = raw_input("Enter date (MM/DD/YYYY): ")
            if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
                print "!Invalid date."
                try_again = raw_input("Try Again? 'Y' for Yes, 'N' for No: ")
                try_again = try_again.upper()
                if (try_again == 'Y'):
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print calendar
        elif user_choice == 'D':
            if len(calendar.keys()) < 1:
                print "The calendar is already empty."
            else:
                event = raw_input("Which event? ")
                for date in calendar.keys():
                    if calendar[date] == event:
                        del(calendar[date])
                        print "Event was succesfully deleted."
                        print calendar
                    else:
                        print "Event does not exist in Calendar."
        elif user_choice == 'X':
            start = False
        else:
            print "Invalid command. "
            start = False



def main():
    start_calendar()


if __name__=="__main__":
    main()

