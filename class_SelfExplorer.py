##查看id
class SelfExplorer:
    def __init__(self, a):

        self.a = a;
        print('init:a=%g, id(self)=%d' %(self.a, id(self)))
    def value(self, x):
        print('value:a=%g, id(self)=%d' %(self.a, id(self)))
        return(self.a*x)
##账户存取款
class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self._no = account_number
        self.__balance = initial_amount
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def dump(self):
        print('%s, %s, balance: %s' %\
              (self.name, self.no, self.balance))
    def get_balance(self):
        print(self.balance)

