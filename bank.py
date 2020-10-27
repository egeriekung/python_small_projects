class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

#thing you can do:P
    
    #add money:P
    def deposit(self, amount):
        self.balance += amount
    
    #take money out:P
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print('No money no honey D:')
    
    #check money:P
    def statement(self):
        print('Your money: £{}'.format(self.balance))

#For the current accounts:P

class Current(Account):
    
    #so ppl can make accounts:P
    def __init__(self,name,balance):
        super().__init__(name, balance, min_balance = -1000)
    
    #to make text more pretty:P
    def __str__(self):
        return '''{}'s Current Account: Balance £{}.'''.format(self.name, self.balance)

#for the savings account:P

class Savings(Account):
    
    #soo ppl can make accounts
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    #to make text more pretty:P
    def __str__(self):
        return '''{}'s Savings Account: Balance £{}.'''.format(self.name, self.balance)

# uncomment to test the code
savings = Savings('Egerie',2000)
print(savings)
current = Current('Egerie',1000)
print(current)
current.withdraw(3000)
print(current)
current.withdraw(200)
print(current)
current.deposit(100)
print(current)
savings.withdraw(500)
print(savings)
savings.withdraw(5000)
print(savings)
savings.deposit(3000)
print(savings)
Account.statement(savings)
Account.statement(current)