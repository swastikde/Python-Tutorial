# =============================================================
# Module 4: Recursion in Python
# =============================================================
# Recursion is a technique where a function calls itself to
# solve a smaller version of the same problem.
#
# Every recursive function needs:
#   1. Base case  — stops the recursion
#   2. Recursive case — reduces the problem toward the base case
#
# Topics Covered:
#   - Basic recursion (factorial, Fibonacci)
#   - Recursion with memoization
#   - Tower of Hanoi
#   - Flatten nested list
#   - Power function
#   - GCD (Euclid's algorithm)
#   - Binary search (recursive)
#   - Recursion vs iteration trade-offs
# =============================================================

import sys
sys.setrecursionlimit(10000)

# ---------------------------------------------------------
# 1. Factorial
# ---------------------------------------------------------
print("=== Factorial ===")

def factorial(n):
    """
    Compute n! recursively.

    Base case:  n <= 1 → return 1
    Recursive:  n * factorial(n-1)

    Time:  O(n)
    Space: O(n) — call stack
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


for i in range(8):
    print(f"  {i}! = {factorial(i)}")

# ---------------------------------------------------------
# 2. Fibonacci Sequence
# ---------------------------------------------------------
print("\n=== Fibonacci ===")

def fib_naive(n):
    """
    Naive recursive Fibonacci.

    Time:  O(2^n) — exponential, very slow for large n
    Space: O(n)
    """
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo=None):
    """
    Memoized Fibonacci — cache previously computed values.

    Time:  O(n)
    Space: O(n)
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


print("First 10 Fibonacci numbers:")
print(f"  naive: {[fib_naive(i) for i in range(10)]}")
print(f"  memo:  {[fib_memo(i) for i in range(10)]}")

# Performance difference
import time
n = 30
t0 = time.perf_counter(); fib_naive(n); naive_time = time.perf_counter() - t0
t0 = time.perf_counter(); fib_memo(n);  memo_time  = time.perf_counter() - t0
print(f"\nfib({n}):")
print(f"  naive: {naive_time*1000:.2f} ms")
print(f"  memo:  {memo_time*1000:.4f} ms")

# ---------------------------------------------------------
# 3. Power Function
# ---------------------------------------------------------
print("\n=== Fast Power (Exponentiation by Squaring) ===")

def power(base, exp):
    """
    Compute base^exp recursively using fast exponentiation.

    Time:  O(log exp)
    Space: O(log exp)
    """
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    return base * power(base, exp - 1)


print(f"  2^10 = {power(2, 10)}")
print(f"  3^5  = {power(3, 5)}")
print(f"  5^0  = {power(5, 0)}")
print(f"  2^-3 = {power(2, -3)}")

# ---------------------------------------------------------
# 4. GCD — Euclid's Algorithm
# ---------------------------------------------------------
print("\n=== GCD (Euclid's Algorithm) ===")

def gcd(a, b):
    """
    Compute greatest common divisor recursively.

    Time:  O(log min(a, b))
    Space: O(log min(a, b))
    """
    if b == 0:
        return a
    return gcd(b, a % b)


pairs = [(48, 18), (100, 75), (7, 5), (0, 5)]
for a, b in pairs:
    print(f"  gcd({a}, {b}) = {gcd(a, b)}")

# ---------------------------------------------------------
# 5. Tower of Hanoi
# ---------------------------------------------------------
print("\n=== Tower of Hanoi ===")

def hanoi(n, source, destination, auxiliary):
    """
    Solve Tower of Hanoi for n disks.

    Moves disks from source to destination using auxiliary peg.
    Minimum moves required: 2^n - 1

    Time:  O(2^n)
    Space: O(n)
    """
    if n == 1:
        print(f"  Move disk 1: {source} → {destination}")
        return
    hanoi(n - 1, source, auxiliary, destination)
    print(f"  Move disk {n}: {source} → {destination}")
    hanoi(n - 1, auxiliary, destination, source)


n_disks = 3
print(f"Solving Tower of Hanoi with {n_disks} disks:")
hanoi(n_disks, "A", "C", "B")
print(f"Total moves: {2**n_disks - 1}")

# ---------------------------------------------------------
# 6. Flatten Nested List
# ---------------------------------------------------------
print("\n=== Flatten Nested List ===")

def flatten(nested):
    """
    Recursively flatten a nested list of any depth.

    Time:  O(n) where n = total number of elements
    Space: O(d) where d = maximum nesting depth
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


nested_list = [1, [2, 3], [4, [5, 6]], [7, [8, [9, 10]]]]
print(f"  Input:  {nested_list}")
print(f"  Output: {flatten(nested_list)}")

# ---------------------------------------------------------
# 7. Recursive Binary Search
# ---------------------------------------------------------
print("\n=== Recursive Binary Search ===")

def binary_search(arr, target, lo=0, hi=None):
    """
    Recursive binary search on a sorted array.

    Time:  O(log n)
    Space: O(log n) — call stack
    """
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, hi)
    else:
        return binary_search(arr, target, lo, mid - 1)


data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
for t in [23, 2, 91, 50]:
    idx = binary_search(data, t)
    print(f"  binary_search({t:>3}) → index {idx}")

# ---------------------------------------------------------
# 8. Recursion vs Iteration trade-offs
# ---------------------------------------------------------
print("\n=== Recursion vs Iteration ===")
print("""
  Recursion                          Iteration
  ----------------------------------+----------------------------------
  Elegant and readable code          More verbose but explicit
  Natural for tree/graph problems    Better for simple loops
  Risk of stack overflow (deep calls) No stack overflow risk
  O(n) stack space (unless TCO)      O(1) stack space
  Python lacks tail-call optimization Use iteration for very deep problems
""")
