class Account:
    def __init__(self):
        self._balance = 0
        
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if(self._balance > amount):
            self._balance -= amount
    
    def __str__(self):
        return f"The bank balance is {self._balance}"