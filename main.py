#implement a class called Bank account that represents a bank account.the class should have private attributes for a account number , account holder name and account balance include method to deposit money, withdraw money and display the account balance.ensure that the account balance that cannot be accessed directly from outside the class.write a program to create an instance of the bank account class and test the deposit and withdraw functionality 
class bankaccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number =account_number
    self.__account_holder_name =account_holder_name
    self.__account_balance =initial_balance

def deposit(self, amount):
  if amount>0:
    self. __account_balance +=amount
    print("deposited ₹ {}.new balance:₹{}". format (amount,self.__account_balance))
  else:
    print ("invalid deposit amount.please deposit a positive amount")
    def withdraw(self, amount ):
      if amount >0 and amount <=self.__account_balance:
        self.__account_balance -=amount
        print ("withdraw ₹{}.new balance:₹{} ". format (amount,self.__account_balance ))
      else:
        print ("invalid withdrawal amount or insufficient balance")
        def display_balance(self):
          print("account balance for {}(account #{}):₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance ))

#create an instance of the Bank account class
account=bankaccount(account_number ="123456789",account_holder_name="thirru", initial_balance=5000.0)
#test deposit and withdraw functionality
account.display_balance()
account.deposit(500.0)
account.withdraw (200.0)
account.display_balance()