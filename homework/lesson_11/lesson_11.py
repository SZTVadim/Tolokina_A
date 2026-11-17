class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        return True if self.pages > 300 else False


book1 = Book(title="Война и мир", author="Толстой", pages=800)
book2 = Book(title="Алёнькины рассказы", author="Пресняков", pages=50)
book3 = Book(title="Айболит", author="Чуковский", pages=300)

print(book1.get_info())
print(book2.is_long())


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Недостаточно средств")
            return False

    def get_balance(self):
        return self.balance


account = BankAccount("Алёна", 0)
print(f"Владелец {account.owner}")
print(f"Начальный баланс {account.get_balance()} руб.")

account.deposit(500)
print(f"Текущий баланс: {account.get_balance()} руб.")

result = account.withdraw(100)
print(f"Успешно? {result}")
print(f"Текущий баланс: {account.get_balance()} руб.")

result = account.withdraw(1000)
print(f"Успешно? {result}")
print(f"Текущий баланс: {account.get_balance()} руб.")
