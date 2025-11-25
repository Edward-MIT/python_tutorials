# Encapsulation and Polymorphism Demo

class BankAccount:
    """Base class demonstrating encapsulation"""

    def __init__(self, account_number, holder_name, balance=0):
        self.__account_number = account_number  # Private attribute (encapsulation)
        self.__balance = balance  # Private attribute (encapsulation)
        self._holder_name = holder_name  # Protected attribute

    # Getter method for balance (encapsulation)
    def get_balance(self):
        return self.__balance

    # Getter method for account number (encapsulation)
    def get_account_number(self):
        return self.__account_number

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount!")

    # Polymorphic method - will be overridden in child classes
    def calculate_interest(self):
        return 0

    # Display account info
    def display_info(self):
        print(f"\n--- Account Info ---")
        print(f"Account Number: {self.__account_number}")
        print(f"Holder: {self._holder_name}")
        print(f"Balance: ${self.__balance}")


class SavingsAccount(BankAccount):
    """Savings account with interest calculation"""

    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.03):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    # Polymorphism: Overriding the calculate_interest method
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Savings Account Interest (3%): ${interest:.2f}")
        return interest

    # Additional method specific to SavingsAccount
    def add_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)


class CheckingAccount(BankAccount):
    """Checking account with overdraft protection"""

    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=100):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    # Polymorphism: Overriding the calculate_interest method
    def calculate_interest(self):
        interest = self.get_balance() * 0.01
        print(f"Checking Account Interest (1%): ${interest:.2f}")
        return interest

    # Polymorphism: Overriding the withdraw method
    def withdraw(self, amount):
        available_funds = self.get_balance() + self.overdraft_limit
        if amount > 0 and amount <= available_funds:
            new_balance = self.get_balance() - amount
            super().deposit(-amount)  # Using parent's method creatively
            print(f"Withdrew ${amount}. Balance: ${new_balance} (Overdraft available: ${self.overdraft_limit})")
        else:
            print(f"Cannot withdraw ${amount}. Exceeds overdraft limit!")


class BusinessAccount(BankAccount):
    """Business account with higher interest and transaction fees"""

    def __init__(self, account_number, holder_name, balance=0, transaction_fee=2):
        super().__init__(account_number, holder_name, balance)
        self.transaction_fee = transaction_fee

    # Polymorphism: Overriding the calculate_interest method
    def calculate_interest(self):
        interest = self.get_balance() * 0.05
        print(f"Business Account Interest (5%): ${interest:.2f}")
        return interest

    # Polymorphism: Overriding the withdraw method with transaction fee
    def withdraw(self, amount):
        total_amount = amount + self.transaction_fee
        if total_amount <= self.get_balance():
            super().withdraw(total_amount)
            print(f"Transaction fee: ${self.transaction_fee}")
        else:
            print(f"Insufficient funds including ${self.transaction_fee} fee!")


# ============================================
# DEMONSTRATION
# ============================================

def process_account_interest(account):
    """
    Polymorphism demonstration: This function works with any BankAccount type
    and calls their specific calculate_interest implementation
    """
    print(f"\nProcessing interest for {account._holder_name}'s account...")
    account.calculate_interest()


if __name__ == "__main__":
    print("=" * 50)
    print("ENCAPSULATION & POLYMORPHISM DEMONSTRATION")
    print("=" * 50)

    # Creating different account objects
    savings = SavingsAccount("SAV001", "Alice Johnson", 1000)
    checking = CheckingAccount("CHK001", "Bob Smith", 500, overdraft_limit=200)
    business = BusinessAccount("BUS001", "Tech Corp", 5000, transaction_fee=5)

    # Encapsulation Demo: Cannot directly access private attributes
    print("\n--- ENCAPSULATION DEMO ---")
    print(f"Savings balance (via getter): ${savings.get_balance()}")
    # print(savings.__balance)  # This would raise an AttributeError!

    # Demonstrating deposit/withdraw
    print("\n--- OPERATIONS DEMO ---")
    savings.deposit(200)
    checking.withdraw(600)  # Uses overdraft
    business.withdraw(100)  # Includes transaction fee

    # Polymorphism Demo 1: Different objects, same method name, different behavior
    print("\n" + "=" * 50)
    print("POLYMORPHISM DEMO 1: Different Interest Calculations")
    print("=" * 50)

    accounts = [savings, checking, business]

    for account in accounts:
        account.calculate_interest()  # Each calculates differently!

    # Polymorphism Demo 2: Using a function that accepts any BankAccount type
    print("\n" + "=" * 50)
    print("POLYMORPHISM DEMO 2: Single Function, Multiple Types")
    print("=" * 50)

    process_account_interest(savings)
    process_account_interest(checking)
    process_account_interest(business)

    # Display all account info
    print("\n" + "=" * 50)
    print("FINAL ACCOUNT INFORMATION")
    print("=" * 50)

    savings.display_info()
    checking.display_info()
    business.display_info()

    # Add interest to savings account
    print("\n--- ADDING INTEREST TO SAVINGS ---")
    savings.add_interest()
    savings.display_info()
