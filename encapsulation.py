class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.name = name
        self.health = stamina * 100
        self.mana = intelligence * 10

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        try:
            if amount < 0:
                raise ValueError
            else:
                self.__balance += amount
        except ValueError:
            return "cannot deposit zero or negative funds"
        
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("cannot withdraw zero or negative funds")
        elif amount > self.__balance:
            raise ValueError("insufficient funds")
        else:
            self.__balance -= amount