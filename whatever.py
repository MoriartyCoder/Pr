def transfer(acc_from, acc_to, transfer_sum):
    if acc_from.account_balance < transfer_sum:
        print("Transaction failed!")
        return

    acc_from.account_balance -= transfer_sum
    acc_to.account_balance += transfer_sum
    print("Transaction succeded!")


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nAge: {self.age}"

    def birthday(self):
        self.age += 1

    def get_married(self, new_last_name):
        self.last_name = new_last_name


p = Person("John", "Smith", 21)
print(p)
p.birthday()
print(p)
p.get_married("Müller")
print(p)


class Account:

    def __init__(self, balance):
        self.account_balance = balance

        print("A new Account has been created!")

    def transfer(self, other_acc, transfer_sum):
        transfer(self, other_acc, transfer_sum)


ac1 = Account(500)
ac2 = Account(100)

transfer(ac1, ac2, 100)
print(f"Ac1: {ac1.account_balance}\nAc2: {ac2.account_balance}\n")

ac1.transfer(ac2, 100)
print(f"Ac1: {ac1.account_balance}\nAc2: {ac2.account_balance}\n")

ac1.transfer(ac2, 50000)
print(f"Ac1: {ac1.account_balance}\nAc2: {ac2.account_balance}\n")


