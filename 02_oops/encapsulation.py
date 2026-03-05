# =============================================================
# Module 2: Encapsulation in Python
# =============================================================
# Topics Covered:
#   - Public, protected, and private attributes
#   - Name mangling for private attributes
#   - Getters and setters (manual)
#   - @property decorator for controlled access
#   - Encapsulation in practice (BankAccount example)
# =============================================================

# ---------------------------------------------------------
# 1. Access Modifiers in Python
# ---------------------------------------------------------
# Python does NOT enforce access control at the language level,
# but uses naming conventions:
#
#   attribute       → public  (accessible everywhere)
#   _attribute      → protected (by convention, internal use)
#   __attribute     → private (name-mangled, harder to access externally)

print("=== Access Levels ===")

class Employee:
    def __init__(self, name, department, salary):
        self.name = name             # public
        self._department = department  # protected (convention)
        self.__salary = salary        # private (name-mangled)

    def get_salary(self):
        """Public method to safely expose private salary."""
        return self.__salary

    def set_salary(self, amount):
        """Validate before setting salary."""
        if amount < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = amount

    def display(self):
        print(f"  Name: {self.name}")
        print(f"  Department: {self._department}")
        print(f"  Salary: ${self.__salary:,.2f}")


emp = Employee("Alice", "Engineering", 85000)
emp.display()

# Public — directly accessible
print(f"\nPublic name: {emp.name}")

# Protected — accessible but flagged as internal
print(f"Protected dept: {emp._department}")

# Private — name-mangled, not directly accessible as __salary
# emp.__salary  # raises AttributeError
print(f"Private via getter: ${emp.get_salary():,.2f}")

# Name mangling: __salary becomes _Employee__salary internally
print(f"Via mangled name: ${emp._Employee__salary:,.2f}")

# ---------------------------------------------------------
# 2. @property — Pythonic Getters/Setters
# ---------------------------------------------------------
print("\n=== @property (Pythonic Getters/Setters) ===")

class Rectangle:
    """Rectangle with validated width and height."""

    def __init__(self, width, height):
        self.width = width      # uses the setter
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError(f"Width must be positive, got {value}.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError(f"Height must be positive, got {value}.")
        self._height = value

    @property
    def area(self):
        """Read-only computed property."""
        return self._width * self._height

    @property
    def perimeter(self):
        """Read-only computed property."""
        return 2 * (self._width + self._height)

    def __str__(self):
        return (f"Rectangle(width={self._width}, height={self._height}, "
                f"area={self.area}, perimeter={self.perimeter})")


r = Rectangle(4, 5)
print(r)

r.width = 10
print(f"After resize: {r}")

try:
    r.width = -1
except ValueError as e:
    print(f"Error: {e}")

# ---------------------------------------------------------
# 3. Practical Example: BankAccount
# ---------------------------------------------------------
print("\n=== Practical Example: BankAccount ===")

class BankAccount:
    """
    Encapsulated bank account.

    Rules:
      - Balance cannot go below zero.
      - Withdrawals are rejected if insufficient funds.
      - Transaction history is maintained internally.
    """

    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        self.__balance = initial_balance
        self.__transactions = []
        self.__record(f"Account opened with ${initial_balance:.2f}")

    def __record(self, description):
        """Private: record a transaction."""
        self.__transactions.append(description)

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        self.__record(f"Deposited: +${amount:.2f} (balance: ${self.__balance:.2f})")
        print(f"  Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            print(f"  Insufficient funds. Balance: ${self.__balance:.2f}")
            return False
        self.__balance -= amount
        self.__record(f"Withdrew:  -${amount:.2f} (balance: ${self.__balance:.2f})")
        print(f"  Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True

    @property
    def balance(self):
        """Read-only balance property."""
        return self.__balance

    def print_statement(self):
        """Print the transaction history."""
        print(f"\n  Account Statement for {self.owner}:")
        print("  " + "-" * 40)
        for tx in self.__transactions:
            print(f"    {tx}")
        print("  " + "-" * 40)
        print(f"    Current Balance: ${self.__balance:.2f}")


account = BankAccount("Alice", 1000.0)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)   # should fail
account.deposit(100)
account.print_statement()
