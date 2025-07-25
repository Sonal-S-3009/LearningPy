'''class BankAc:
    def __init__(self):
        self.balance = 0.0
    def deposit(self,amount):
        self.balance += amount
    def withdrawal(self,amount):
        if amount > self.balance:
            print("Withdrawal amount exceeds the balance")
        else:
            self.balance -= amount
    def display_balance(self):
        if self.balance >0:
         print(f"Balance Amount: {self.balance}")
        else:
            print("Zero Balance")


passbook = BankAc()
passbook.deposit(5000)
passbook.display_balance()
passbook.withdrawal(2000)
passbook.display_balance()
passbook.withdrawal(4000)
passbook.display_balance()'''

class Vehicle:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"This is vehicle: {self.name}"

class Car(Vehicle):
    def __init__(self,name):
        super().__init__(name)
        self.name = name
    def __str__(self):
        return "this is car: {self.name}"

class Truck(Vehicle):
    def __init__(self,name):
        super().__init__(name)
        self.name = name
    def __str__(self):
        return f"this is Truck: {self.name}"

obj = Truck("Mahindra")
print(obj)