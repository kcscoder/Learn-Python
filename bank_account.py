"""
Codecademy < Learn Python 
11 Introduction to Classes
=======================================================
Bank Account
=======================================================
The bank account allows you to:
    - Accept deposits
    - Allow withdrawals
    - Show the balance
    - Show the details of the acount
"""

class BankAccount(object):
    balance = 0
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "Owner: %s \ Balance: $%.2f" % (self.name, self.balance)
    def show_balance(self):
        print "%.2f" % self.balance
  
    def deposit(self, amount):
        if (amount <= 0):
            print "Error. Deposit too small."
        else:
            print "Depositing $%.2f" % (amount)
            self.balance += amount
            self.show_balance()
      
    def withdraw(self, amount):
        if (amount > self.balance):
            print "Error. Withdrawal exceeds balance."
        else:
	    print "Withdrawing $%.2f" %  (amount)
            self.balance -= amount
            self.show_balance()

def main():
    my_account = BankAccount("Bernard")
    print my_account
    my_account.show_balance()
    my_account.deposit(2000)
    my_account.withdraw(1000)
    print my_account

if __name__=="__main__":
    main()
      
