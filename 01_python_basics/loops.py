# =============================================================
# Module 1: Loops and Control Flow in Python
# =============================================================
# Topics Covered:
#   - for loop (with range, sequences, enumerate, zip)
#   - while loop
#   - break, continue, pass
#   - else clause on loops
#   - Nested loops
#   - List comprehensions
# =============================================================

# ---------------------------------------------------------
# 1. for Loop
# ---------------------------------------------------------
print("=== for Loop ===")

# Iterating with range()
print("Counting 1 to 5:")
for i in range(1, 6):
    print(f"  {i}", end=" ")
print()

# range(start, stop, step)
print("Even numbers 0-10:")
for i in range(0, 11, 2):
    print(f"  {i}", end=" ")
print()

# Iterating over a list
fruits = ["apple", "banana", "cherry", "date"]
print("\nIterating over a list:")
for fruit in fruits:
    print(f"  {fruit}")

# enumerate() — get index + value
print("\nUsing enumerate():")
for idx, fruit in enumerate(fruits, start=1):
    print(f"  {idx}. {fruit}")

# zip() — iterate over multiple sequences together
names = ["Alice", "Bob", "Charlie"]
scores = [88, 95, 72]
print("\nUsing zip():")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# ---------------------------------------------------------
# 2. while Loop
# ---------------------------------------------------------
print("\n=== while Loop ===")

# Basic while loop
count = 1
print("Counting up with while:")
while count <= 5:
    print(f"  {count}", end=" ")
    count += 1
print()

# Countdown
n = 5
print("\nCountdown:")
while n > 0:
    print(f"  {n}", end=" ")
    n -= 1
print("  Liftoff! 🚀")

# User-input simulation (deterministic example)
print("\nSimulating input validation:")
valid_inputs = [0, -1, 5]   # 5 is the valid value
attempt = 0
user_input = 0
while user_input <= 0:
    user_input = valid_inputs[attempt]
    attempt += 1
    if user_input <= 0:
        print(f"  Invalid input ({user_input}). Try again.")
print(f"  Valid input received: {user_input}")

# ---------------------------------------------------------
# 3. break — Exit the loop early
# ---------------------------------------------------------
print("\n=== break ===")

print("Find first even number > 10 in list:")
numbers = [3, 7, 11, 14, 18, 21]
for num in numbers:
    if num > 10 and num % 2 == 0:
        print(f"  Found: {num}")
        break

# ---------------------------------------------------------
# 4. continue — Skip current iteration
# ---------------------------------------------------------
print("\n=== continue ===")

print("Print only odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue        # skip even numbers
    print(f"  {i}", end=" ")
print()

# ---------------------------------------------------------
# 5. pass — Do nothing (placeholder)
# ---------------------------------------------------------
print("\n=== pass ===")

print("Loop with pass (placeholder logic):")
for i in range(5):
    if i == 3:
        pass    # TODO: handle special case
    else:
        print(f"  Processing {i}")

# ---------------------------------------------------------
# 6. else Clause on Loops
# ---------------------------------------------------------
print("\n=== else Clause on Loops ===")

# The else block runs only if the loop completed without break
print("Search for 7 in list [1, 3, 5, 9]:")
target = 7
for num in [1, 3, 5, 9]:
    if num == target:
        print(f"  Found {target}!")
        break
else:
    print(f"  {target} not found in list.")

print("\nSearch for 3 in list [1, 3, 5, 9]:")
target = 3
for num in [1, 3, 5, 9]:
    if num == target:
        print(f"  Found {target}!")
        break
else:
    print(f"  {target} not found in list.")

# ---------------------------------------------------------
# 7. Nested Loops
# ---------------------------------------------------------
print("\n=== Nested Loops ===")

print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i}×{j}={i*j}", end="  ")
    print()

print("\nPattern — right triangle:")
rows = 5
for i in range(1, rows + 1):
    print("  " + "* " * i)

# ---------------------------------------------------------
# 8. List Comprehensions
# ---------------------------------------------------------
print("\n=== List Comprehensions ===")

# Basic: [expression for item in iterable]
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares 1-5:         {squares}")

# With condition: [expression for item in iterable if condition]
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares 1-10:   {even_squares}")

# Nested list comprehension — flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [val for row in matrix for val in row]
print(f"Flattened matrix:    {flat}")

# Dictionary comprehension
word = "hello"
char_count = {ch: word.count(ch) for ch in set(word)}
print(f"Char count in 'hello': {char_count}")

# Set comprehension
unique_lengths = {len(fruit) for fruit in fruits}
print(f"Unique fruit name lengths: {unique_lengths}")
