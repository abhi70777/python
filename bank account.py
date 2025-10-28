class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __add__(self, other):
        return self._balance + other._balance


class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05


class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02
    
savings = SavingsAccount("Ravi", 10000)
current = CurrentAccount("Anjali", 15000)

print("Account Details:")
print(f"Name: {savings._name}, Balance: {savings._balance}, Interest: {savings.calculate_interest()}")
print(f"Name: {current._name}, Balance: {current._balance}, Interest: {current.calculate_interest()}")

total_balance = savings + current
print(f"\nTotal Balance (Ravi + Anjali): {total_balance}")
