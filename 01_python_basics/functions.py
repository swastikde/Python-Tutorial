# =============================================================
# Module 1: Functions in Python
# =============================================================
# Topics Covered:
#   - Defining and calling functions
#   - Parameters: positional, keyword, default, *args, **kwargs
#   - Return values
#   - Scope (local vs global)
#   - Lambda functions
#   - Higher-order functions: map, filter, sorted
#   - Docstrings
#   - Recursive functions
# =============================================================

# ---------------------------------------------------------
# 1. Defining and Calling Functions
# ---------------------------------------------------------
print("=== Defining and Calling Functions ===")

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))

# Function with no return value (implicitly returns None)
def print_separator(char="-", length=40):
    print(char * length)

print_separator()
print_separator("=", 20)

# ---------------------------------------------------------
# 2. Parameters: Positional, Keyword, Default
# ---------------------------------------------------------
print("\n=== Parameters ===")

def describe_person(name, age, city="Unknown"):
    """Describe a person with name, age, and optional city."""
    return f"{name}, age {age}, from {city}"

# Positional arguments
print(describe_person("Alice", 30, "New York"))

# Keyword arguments (order doesn't matter)
print(describe_person(age=25, name="Bob", city="London"))

# Default parameter used
print(describe_person("Charlie", 22))

# ---------------------------------------------------------
# 3. *args — Variable Positional Arguments
# ---------------------------------------------------------
print("\n=== *args ===")

def add_all(*numbers):
    """Return the sum of any number of arguments."""
    return sum(numbers)

print(f"add_all(1, 2, 3)        = {add_all(1, 2, 3)}")
print(f"add_all(10, 20, 30, 40) = {add_all(10, 20, 30, 40)}")
print(f"add_all()               = {add_all()}")

# ---------------------------------------------------------
# 4. **kwargs — Variable Keyword Arguments
# ---------------------------------------------------------
print("\n=== **kwargs ===")

def print_profile(**info):
    """Print all key-value pairs passed as keyword arguments."""
    for key, value in info.items():
        print(f"  {key}: {value}")

print("Profile 1:")
print_profile(name="Alice", age=30, job="Engineer")

print("Profile 2:")
print_profile(name="Bob", hobby="chess", city="Paris", level="beginner")

# ---------------------------------------------------------
# 5. Combined Parameters
# ---------------------------------------------------------
print("\n=== Combined Parameters ===")

def mixed(a, b, *args, keyword="default", **kwargs):
    """Demonstrate all parameter types together."""
    print(f"  a={a}, b={b}, args={args}, keyword={keyword}, kwargs={kwargs}")

mixed(1, 2)
mixed(1, 2, 3, 4, 5)
mixed(1, 2, 3, keyword="custom", extra="value")

# ---------------------------------------------------------
# 6. Return Values
# ---------------------------------------------------------
print("\n=== Return Values ===")

def min_max(numbers):
    """Return both minimum and maximum of a list."""
    return min(numbers), max(numbers)   # returns a tuple

low, high = min_max([3, 1, 7, 2, 9, 4])
print(f"min={low}, max={high}")

# Early return
def safe_divide(a, b):
    """Divide a by b; return None if b is zero."""
    if b == 0:
        return None
    return a / b

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

# ---------------------------------------------------------
# 7. Variable Scope (Local vs Global)
# ---------------------------------------------------------
print("\n=== Scope ===")

counter = 0     # global variable

def increment():
    global counter  # declare intent to modify global variable
    counter += 1

increment()
increment()
increment()
print(f"counter after 3 increments: {counter}")

def scope_demo():
    local_var = "I am local"
    print(f"  Inside function: {local_var}")

scope_demo()
# print(local_var)  # would raise NameError: local_var not defined here

# ---------------------------------------------------------
# 8. Lambda Functions
# ---------------------------------------------------------
print("\n=== Lambda Functions ===")

# lambda <args>: <expression>
square = lambda x: x ** 2
add = lambda x, y: x + y

print(f"square(5) = {square(5)}")
print(f"add(3, 4) = {add(3, 4)}")

# Commonly used inline with map/filter/sorted
numbers = [4, 1, 9, 3, 7, 2]
sorted_nums = sorted(numbers, key=lambda x: -x)   # descending
print(f"Sorted descending: {sorted_nums}")

# ---------------------------------------------------------
# 9. Higher-Order Functions: map, filter
# ---------------------------------------------------------
print("\n=== Higher-Order Functions ===")

nums = [1, 2, 3, 4, 5, 6, 7, 8]

# map — apply function to every element
squared = list(map(lambda x: x ** 2, nums))
print(f"Squared:     {squared}")

# filter — keep elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Evens only:  {evens}")

# sorted with key
words = ["banana", "apple", "cherry", "date"]
by_length = sorted(words, key=len)
print(f"By length:   {by_length}")

# ---------------------------------------------------------
# 10. Recursive Functions
# ---------------------------------------------------------
print("\n=== Recursion ===")

def factorial(n):
    """Compute n! recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

for i in range(1, 8):
    print(f"  {i}! = {factorial(i)}")

def fibonacci(n):
    """Return nth Fibonacci number (0-indexed) recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fib_sequence = [fibonacci(i) for i in range(10)]
print(f"\nFibonacci(0-9): {fib_sequence}")

# ---------------------------------------------------------
# 11. Docstrings
# ---------------------------------------------------------
print("\n=== Docstrings ===")

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area (length * width).

    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width

print(f"Area of 5x3 rectangle: {calculate_area(5, 3)}")
print(f"\nDocstring:\n{calculate_area.__doc__}")
