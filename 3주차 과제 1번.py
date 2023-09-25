class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"{self.name}({self.balance}원)"
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        return self.balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

if __name__ == '__main__':
    c1 = Customer('Bill')
    c2 = Customer('Steve', 50000)
    c3 = Customer('Tim', 100000)
    print(c1, c2, c3)

    c1.deposit(50000)
    c2.deposit(30000)
    c3.withdraw(100000)
    print(c1, c2, c3)

    c2.withdraw(1000000)
    print(c1, c2, c3)
