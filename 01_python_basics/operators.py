# =============================================================
# Module 1: Operators in Python
# =============================================================
# Topics Covered:
#   - Arithmetic operators
#   - Comparison (relational) operators
#   - Logical operators
#   - Bitwise operators
#   - Assignment operators
#   - Identity operators (is, is not)
#   - Membership operators (in, not in)
#   - Operator precedence
# =============================================================

# ---------------------------------------------------------
# 1. Arithmetic Operators
# ---------------------------------------------------------
print("=== Arithmetic Operators ===")
a, b = 15, 4

print(f"a={a}, b={b}")
print(f"  a + b  = {a + b}")    # Addition
print(f"  a - b  = {a - b}")    # Subtraction
print(f"  a * b  = {a * b}")    # Multiplication
print(f"  a / b  = {a / b}")    # True division (returns float)
print(f"  a // b = {a // b}")   # Floor division
print(f"  a % b  = {a % b}")    # Modulo (remainder)
print(f"  a ** b = {a ** b}")   # Exponentiation

# ---------------------------------------------------------
# 2. Comparison (Relational) Operators
# ---------------------------------------------------------
print("\n=== Comparison Operators ===")
x, y = 10, 20

print(f"x={x}, y={y}")
print(f"  x == y : {x == y}")   # Equal
print(f"  x != y : {x != y}")   # Not equal
print(f"  x <  y : {x < y}")    # Less than
print(f"  x >  y : {x > y}")    # Greater than
print(f"  x <= y : {x <= y}")   # Less than or equal
print(f"  x >= y : {x >= y}")   # Greater than or equal

# ---------------------------------------------------------
# 3. Logical Operators
# ---------------------------------------------------------
print("\n=== Logical Operators ===")

p, q = True, False
print(f"p={p}, q={q}")
print(f"  p and q : {p and q}")
print(f"  p or  q : {p or q}")
print(f"  not p   : {not p}")

# Short-circuit evaluation
print("\nShort-circuit evaluation:")
print(f"  False and (1/0)  → won't raise ZeroDivisionError")
result = False and (1 / 0 if False else 0)
print(f"  result = {result}")

# ---------------------------------------------------------
# 4. Bitwise Operators
# ---------------------------------------------------------
print("\n=== Bitwise Operators ===")
m, n = 12, 10   # 12 = 1100, 10 = 1010 in binary

print(f"m={m} ({bin(m)}), n={n} ({bin(n)})")
print(f"  m & n  = {m & n}  ({bin(m & n)})   AND")
print(f"  m | n  = {m | n}  ({bin(m | n)})  OR")
print(f"  m ^ n  = {m ^ n}  ({bin(m ^ n)})   XOR")
print(f"  ~m     = {~m}            NOT")
print(f"  m << 1 = {m << 1}  ({bin(m << 1)})  Left shift")
print(f"  m >> 1 = {m >> 1}  ({bin(m >> 1)})   Right shift")

# ---------------------------------------------------------
# 5. Assignment Operators
# ---------------------------------------------------------
print("\n=== Assignment Operators ===")

val = 10
print(f"Initial val = {val}")

val += 5;  print(f"  val += 5  → {val}")
val -= 3;  print(f"  val -= 3  → {val}")
val *= 2;  print(f"  val *= 2  → {val}")
val /= 4;  print(f"  val /= 4  → {val}")
val = int(val)
val //= 2; print(f"  val //= 2 → {val}")
val %= 3;  print(f"  val %%= 3  → {val}")
val **= 4; print(f"  val **= 4 → {val}")

# ---------------------------------------------------------
# 6. Identity Operators
# ---------------------------------------------------------
print("\n=== Identity Operators ===")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list2 : {list1 is list2}")   # Different objects
print(f"list1 is list3 : {list1 is list3}")   # Same object
print(f"list1 is not list2 : {list1 is not list2}")

# Small integers are cached by Python
a_int = 256
b_int = 256
print(f"\n256 is 256 : {a_int is b_int}")     # True (cached)

# ---------------------------------------------------------
# 7. Membership Operators
# ---------------------------------------------------------
print("\n=== Membership Operators ===")

fruits = ["apple", "banana", "cherry"]
print(f"fruits = {fruits}")
print(f"  'apple'  in fruits     : {'apple' in fruits}")
print(f"  'grape'  in fruits     : {'grape' in fruits}")
print(f"  'grape'  not in fruits : {'grape' not in fruits}")

# Works on strings too
sentence = "Python is awesome"
print(f"\n  'Python' in '{sentence}': {'Python' in sentence}")
print(f"  'Java'   in '{sentence}': {'Java' in sentence}")

# ---------------------------------------------------------
# 8. Operator Precedence (PEMDAS/BODMAS)
# ---------------------------------------------------------
print("\n=== Operator Precedence ===")
# Highest to lowest: ** > ~ + - (unary) > * / // % > + - > << >> > & > ^ > | > comparisons > not > and > or

expr1 = 2 + 3 * 4       # 14, not 20 (multiplication first)
expr2 = (2 + 3) * 4     # 20
expr3 = 2 ** 3 ** 2     # 2 ** (3 ** 2) = 2 ** 9 = 512 (right-associative)
expr4 = 10 - 4 - 2      # (10 - 4) - 2 = 4 (left-associative)

print(f"  2 + 3 * 4   = {expr1}")
print(f"  (2+3) * 4   = {expr2}")
print(f"  2 ** 3 ** 2 = {expr3}  (right-associative)")
print(f"  10 - 4 - 2  = {expr4}  (left-associative)")
