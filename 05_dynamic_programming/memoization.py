# =============================================================
# Module 5: Dynamic Programming — Memoization (Top-Down)
# =============================================================
# Memoization = caching the results of expensive function calls
# so we don't recompute them.
#
# Approach: Start from the original problem, recurse down to
# subproblems, and store results in a cache.
#
# Pattern:
#   def dp(params):
#       if params in memo: return memo[params]
#       if base_case: return base_value
#       result = ... recursive calls using dp() ...
#       memo[params] = result
#       return result
#
# Topics Covered:
#   - Fibonacci (memoized)
#   - Climbing Stairs
#   - Coin Change (minimum coins)
#   - 0/1 Knapsack
#   - Longest Common Subsequence (LCS)
#   - Using functools.lru_cache
# =============================================================

from functools import lru_cache

# ---------------------------------------------------------
# 1. Fibonacci with Memoization
# ---------------------------------------------------------
print("=== Fibonacci — Memoization ===")

def fib(n, memo=None):
    """
    nth Fibonacci number using top-down memoization.

    Time:  O(n)
    Space: O(n)
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


# Using lru_cache — the Pythonic way
@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


print("Manual memoization:")
print(f"  fib(10) = {fib(10)}")
print(f"  fib(40) = {fib(40)}")

print("\n@lru_cache:")
print(f"  fib_cached(10) = {fib_cached(10)}")
print(f"  fib_cached(40) = {fib_cached(40)}")
print(f"  Cache info: {fib_cached.cache_info()}")

# ---------------------------------------------------------
# 2. Climbing Stairs
# ---------------------------------------------------------
print("\n=== Climbing Stairs ===")

def climb_stairs(n, memo=None):
    """
    Count ways to climb n stairs, taking 1 or 2 steps at a time.

    This is equivalent to Fibonacci(n+1).

    Time:  O(n)
    Space: O(n)
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return n
    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    return memo[n]


for stairs in range(1, 8):
    print(f"  climb_stairs({stairs}) = {climb_stairs(stairs)} ways")

# ---------------------------------------------------------
# 3. Coin Change — Minimum Coins
# ---------------------------------------------------------
print("\n=== Coin Change (Minimum Coins) ===")

def coin_change(coins, amount, memo=None):
    """
    Find the minimum number of coins to make up the amount.

    Returns -1 if the amount cannot be made.

    Time:  O(amount * len(coins))
    Space: O(amount)
    """
    if memo is None:
        memo = {}
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        result = coin_change(coins, amount - coin, memo)
        min_coins = min(min_coins, result + 1)

    memo[amount] = min_coins if min_coins != float('inf') else -1
    return memo[amount]


coins_set = [1, 5, 10, 25]
for amt in [0, 11, 30, 41, 100]:
    result = coin_change(coins_set, amt)
    print(f"  coins={coins_set}, amount={amt:>3} → {result} coins")

print()
coins2 = [2]
print(f"  coins={coins2}, amount=3 → {coin_change(coins2, 3)} (impossible)")

# ---------------------------------------------------------
# 4. 0/1 Knapsack
# ---------------------------------------------------------
print("\n=== 0/1 Knapsack ===")

def knapsack(weights, values, capacity, n=None, memo=None):
    """
    0/1 Knapsack: maximize value without exceeding weight capacity.
    Each item can be taken at most once.

    Args:
        weights (list[int]): Weight of each item.
        values  (list[int]): Value of each item.
        capacity (int):      Maximum weight the knapsack can hold.
        n (int):             Number of items remaining to consider.

    Returns:
        int: Maximum value achievable.

    Time:  O(n * capacity)
    Space: O(n * capacity) — memo table
    """
    if n is None:
        n = len(weights)
    if memo is None:
        memo = {}

    if (n, capacity) in memo:
        return memo[(n, capacity)]
    if n == 0 or capacity == 0:
        return 0

    # Don't take item n-1
    exclude = knapsack(weights, values, capacity, n - 1, memo)

    # Take item n-1 (only if it fits)
    include = 0
    if weights[n - 1] <= capacity:
        include = values[n - 1] + knapsack(
            weights, values, capacity - weights[n - 1], n - 1, memo
        )

    memo[(n, capacity)] = max(exclude, include)
    return memo[(n, capacity)]


weights = [2, 3, 4, 5]
values  = [3, 4, 5, 6]
cap = 5

result = knapsack(weights, values, cap)
print(f"  weights={weights}")
print(f"  values= {values}")
print(f"  capacity={cap} → max value = {result}")

# Larger example
w2 = [1, 2, 3, 5]
v2 = [1, 6, 10, 16]
c2 = 7
print(f"\n  weights={w2}, values={v2}, capacity={c2} → {knapsack(w2, v2, c2)}")

# ---------------------------------------------------------
# 5. Longest Common Subsequence (LCS)
# ---------------------------------------------------------
print("\n=== Longest Common Subsequence (LCS) ===")

def lcs_length(s1, s2, i=None, j=None, memo=None):
    """
    Length of the longest common subsequence of s1 and s2.

    Time:  O(m * n)
    Space: O(m * n) — memo table
    """
    if i is None:
        i = len(s1)
    if j is None:
        j = len(s2)
    if memo is None:
        memo = {}

    if (i, j) in memo:
        return memo[(i, j)]
    if i == 0 or j == 0:
        return 0

    if s1[i - 1] == s2[j - 1]:
        result = 1 + lcs_length(s1, s2, i - 1, j - 1, memo)
    else:
        result = max(
            lcs_length(s1, s2, i - 1, j, memo),
            lcs_length(s1, s2, i, j - 1, memo)
        )

    memo[(i, j)] = result
    return result


lcs_pairs = [
    ("ABCBDAB", "BDCAB"),
    ("AGGTAB",  "GXTXAYB"),
    ("abcde",   "ace"),
]

for s1, s2 in lcs_pairs:
    length = lcs_length(s1, s2)
    print(f"  LCS('{s1}', '{s2}') = {length}")
