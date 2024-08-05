# ---------------- Task 1 ---------------------

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle with sides {self.width} and {self.height}"

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return (self.width + self.height) * 2


new_rectangle = Rectangle(4, 5)

print(new_rectangle)
print(new_rectangle.calculate_area())
print(new_rectangle.calculate_perimeter())
print(new_rectangle.__repr__())


# ---------------- Task 2 ---------------------

class BankAccount:
    balance = 0

    def __init__(self, account_number):
        self.account_number = account_number

    def __str__(self):
        return f"Account number: {self.account_number}, current balans: {self.balance}"

    def deposit(self, summ):
        if summ <= 0:
            print("Wrong summa")
        else:
            self.balance += summ

    def withdraw(self, summ):
        if summ > self.balance:
            print("Sum is bigger then you balance")
        else:
            self.balance = self.balance - summ


new_account = BankAccount("FG25414756")
new_account.deposit(1500)
new_account.withdraw(583)
print(new_account)

