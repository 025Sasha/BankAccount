class BankAccount:
    def __init__(self, owner: str, balance: int = 0):
        if not isinstance(balance, (int, float)) or isinstance(balance, bool):
            raise TypeError("Balance must be an integer or float")
        if balance < 0:
            raise ValueError("Balance can't be negative")
        if not isinstance(owner, str):
            raise TypeError("Owner must be a string")
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount: int, log: bool = True):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        if log:
            self.history.append(f"DEPOSIT +{amount}")

    def withdraw(self, amount: int, log: bool = True):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Not enough money")
        self.balance -= amount
        if log:
            self.history.append(f"WITHDRAW -{amount}")

    def transfer_to(self, other: "BankAccount", amount: int):
        self.withdraw(amount, log=False)
        self.history.append(f"TRANSFER_OUT -{amount} to {other.owner}")
        other.deposit(amount, log=False)
        other.history.append(f"TRANSFER_IN +{amount} from {self.owner}")
    
    def get_balance(self) -> int:
        return self.balance
    
    def last(self,n: int):
        return self.history[-n:]


# a = BankAccount("Sasha", 100)
# b = BankAccount("Masha", 10)

# a.deposit(50)          # баланс a: 150
# a.withdraw(20)         # баланс a: 130
# a.transfer_to(b, 30)   # a: 100, b: 40

# print(a.get_balance()) # 100
# print(b.get_balance()) # 40
# print(a.owner, a.balance, a.history)     # ['Sasha', 100, 'DEPOSIT +50', 'WITHDRAW -20', 'TRANSFER_OUT -30 to Masha']
# print(b.owner,  b.balance, b.history)     # ['Masha', 10, 'TRANSFER_IN +30 from Sasha']
# print(a.last(2))     # ['DEPOSIT +50', 'WITHDRAW -20'] 