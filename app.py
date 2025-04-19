from dataclasses import dataclass

@dataclass
class user:
    username: str
    password: str
    account_number: str
    balance: float
Acount = user("Farhana yousuf", "Farhana123", "1234567890", 10000.0)

account = {
    'username': 'Farhana yousuf',
    "password": 'Farhana123',
    "account_number": '1234567890',
    "balance": 10000.0,
}
print("Welcome to the ATM")
print("Please enter your username and password to access your account.")


@dataclass
Class_Account():
    name: str
    Account_number: int
    def deposits(self, amount ,int): 
        self.balance = amount + self.balance
        print("Depositing {self.balance}")


              
      def deposits(self, amount ,int): 
        self.balance = self.balance + amount
        print("Depositing {amount}")
                      
farhana = Account ("Farhana yousuf", 1234567890)
farhana.deposits(1000)
print(farhana.balance ) 