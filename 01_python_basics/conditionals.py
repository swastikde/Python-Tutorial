# =============================================================
# Module 1: Conditional Statements in Python
# =============================================================
# Topics Covered:
#   - if / elif / else
#   - Nested conditionals
#   - Ternary (conditional) expression
#   - match-case (Python 3.10+)
# =============================================================

# ---------------------------------------------------------
# 1. Basic if / elif / else
# ---------------------------------------------------------
print("=== Basic if / elif / else ===")

score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} → Grade: {grade}")

# ---------------------------------------------------------
# 2. Nested Conditionals
# ---------------------------------------------------------
print("\n=== Nested Conditionals ===")

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted: adult with ID.")
    else:
        print("Access denied: adult but no ID.")
else:
    print("Access denied: underage.")

# ---------------------------------------------------------
# 3. Ternary (Conditional) Expression
# ---------------------------------------------------------
print("\n=== Ternary Expression ===")

# Syntax: <value_if_true> if <condition> else <value_if_false>
temperature = 35
weather = "hot" if temperature > 30 else "comfortable"
print(f"Temperature {temperature}°C → weather is {weather}")

# Chained ternary (use sparingly for readability)
x = 0
sign = "positive" if x > 0 else ("negative" if x < 0 else "zero")
print(f"x = {x} → {sign}")

# ---------------------------------------------------------
# 4. Truthy and Falsy Values
# ---------------------------------------------------------
print("\n=== Truthy and Falsy Values ===")

falsy_values = [0, 0.0, "", [], {}, set(), None, False]
print("Falsy values in Python:")
for v in falsy_values:
    if not v:
        print(f"  {repr(v):<10} → falsy")

# Everything else is truthy
truthy_examples = [1, -1, "hello", [0], {"key": "val"}, True]
print("\nTruthy examples:")
for v in truthy_examples:
    if v:
        print(f"  {repr(v):<15} → truthy")

# ---------------------------------------------------------
# 5. match-case (Python 3.10+)
# ---------------------------------------------------------
print("\n=== match-case (Python 3.10+) ===")

import sys

def describe_command(command):
    match command:
        case "quit":
            return "Quitting the program."
        case "help":
            return "Showing help menu."
        case "start" | "run":
            return "Starting the process."
        case _:
            return f"Unknown command: '{command}'"

for cmd in ["start", "help", "quit", "pause", "run"]:
    print(f"  '{cmd}' → {describe_command(cmd)}")

# match with guards (conditions)
print("\nmatch with guard conditions:")

def classify_number(n):
    match n:
        case n if n < 0:
            return "negative"
        case 0:
            return "zero"
        case n if n % 2 == 0:
            return "positive even"
        case _:
            return "positive odd"

for num in [-5, 0, 4, 7]:
    print(f"  {num:>4} → {classify_number(num)}")

# ---------------------------------------------------------
# 6. Practical Example: Simple Grade Calculator
# ---------------------------------------------------------
print("\n=== Practical Example: Grade Calculator ===")

def get_grade(score):
    """Return letter grade and remark for a given score (0-100)."""
    if not (0 <= score <= 100):
        return "Invalid", "Score must be between 0 and 100"
    elif score >= 90:
        return "A", "Excellent"
    elif score >= 80:
        return "B", "Good"
    elif score >= 70:
        return "C", "Average"
    elif score >= 60:
        return "D", "Below average"
    else:
        return "F", "Fail"

test_scores = [95, 82, 71, 65, 45, -5, 110]
for s in test_scores:
    grade, remark = get_grade(s)
    print(f"  Score {s:>4} → Grade: {grade}, Remark: {remark}")
