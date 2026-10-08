class BankAccount:
  def __init__(self, account_number, balance):
    self.__account_number = account_number
    self.__balance = balance #I am try to remember what to do
  def set_account_number(self, account_number):
    print("Account 1")
    print("Account Number:", self.__account_number)
    print("Balance:", self.__balance)
  def set_balance(self, balance): #Note that it cant be negative
    if balance > 0:
      self.__balance
    else:
      print("The balance must not be a negative number. Please try again.")
  def get_account_number(self):
    print("Account Number:", self.__account_number)
  def get_balance(self):
    print("Balance:", self.__balance)

a1 = BankAccount(12345, 1000)
a1.set_account_number()
a1.get_account_number()
a1.get_balance()
