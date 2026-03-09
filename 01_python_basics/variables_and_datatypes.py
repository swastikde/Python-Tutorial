# =============================================================
# Module 1: Variables and Data Types in Python
# =============================================================
# Topics Covered:
#   - Variable assignment
#   - Numeric types: int, float, complex
#   - String type
#   - Boolean type
#   - None type
#   - Type checking with type() and isinstance()
#   - Type conversion (casting)
# =============================================================

# ---------------------------------------------------------
# 1. Variable Assignment
# ---------------------------------------------------------
# Variables in Python are dynamically typed — no need to
# declare a type explicitly.

name = "Alice"          # str
age = 25                # int
height = 5.7            # float
is_student = True       # bool
nothing = None          # NoneType

print("=== Variable Assignment ===")
print(f"name={name}, age={age}, height={height}, "
      f"is_student={is_student}, nothing={nothing}")

# ---------------------------------------------------------
# 2. Numeric Types
# ---------------------------------------------------------
print("\n=== Numeric Types ===")

x_int = 42
x_float = 3.14
x_complex = 2 + 3j

print(f"int:     {x_int}      → type: {type(x_int)}")
print(f"float:   {x_float}   → type: {type(x_float)}")
print(f"complex: {x_complex}  → type: {type(x_complex)}")

# Basic arithmetic
print(f"\nArithmetic on integers:")
print(f"  10 + 3 = {10 + 3}")
print(f"  10 - 3 = {10 - 3}")
print(f"  10 * 3 = {10 * 3}")
print(f"  10 / 3 = {10 / 3}   (true division → float)")
print(f"  10 // 3 = {10 // 3}  (floor division → int)")
print(f"  10 % 3 = {10 % 3}   (modulo)")
print(f"  10 ** 3 = {10 ** 3} (exponentiation)")

# ---------------------------------------------------------
# 3. String Type
# ---------------------------------------------------------
print("\n=== String Type ===")

greeting = "Hello, World!"
multiline = """This is
a multiline
string."""

print(f"greeting:  {greeting}")
print(f"length:    {len(greeting)}")
print(f"uppercase: {greeting.upper()}")
print(f"lowercase: {greeting.lower()}")
print(f"slice [0:5]: {greeting[0:5]}")
print(f"replace:   {greeting.replace('World', 'Python')}")
print(f"multiline:\n{multiline}")

# String formatting
pi = 3.14159
print(f"\nFormatted float: {pi:.2f}")

# ---------------------------------------------------------
# 4. Boolean Type
# ---------------------------------------------------------
print("\n=== Boolean Type ===")

t = True
f = False

print(f"True and False = {t and f}")
print(f"True or  False = {t or f}")
print(f"not True       = {not t}")

# Booleans behave as integers (True=1, False=0)
print(f"True + True    = {True + True}")
print(f"True * 5       = {True * 5}")

# ---------------------------------------------------------
# 5. None Type
# ---------------------------------------------------------
print("\n=== None Type ===")

value = None
print(f"value is None: {value is None}")
print(f"type(None):    {type(None)}")

# ---------------------------------------------------------
# 6. Type Checking
# ---------------------------------------------------------
print("\n=== Type Checking ===")

samples = [42, 3.14, "hello", True, None, 2 + 3j]
for s in samples:
    print(f"  {str(s):<10} → type: {type(s).__name__}")

# isinstance() is preferred over type() for type checking
print(f"\nisinstance(42, int):   {isinstance(42, int)}")
print(f"isinstance(42, float): {isinstance(42, float)}")
print(f"isinstance(True, int): {isinstance(True, int)}")  # bool is subclass of int

# ---------------------------------------------------------
# 7. Type Conversion (Casting)
# ---------------------------------------------------------
print("\n=== Type Conversion ===")

print(f"int('42')      = {int('42')}")
print(f"float('3.14')  = {float('3.14')}")
print(f"str(100)       = '{str(100)}'")
print(f"bool(0)        = {bool(0)}")
print(f"bool(1)        = {bool(1)}")
print(f"bool('')       = {bool('')}")
print(f"bool('hello')  = {bool('hello')}")
print(f"int(True)      = {int(True)}")
print(f"int(False)     = {int(False)}")
