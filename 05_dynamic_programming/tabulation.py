# =============================================================
# Module 5: Dynamic Programming — Tabulation (Bottom-Up)
# =============================================================
# Tabulation = fill a table (usually a 1D or 2D array) starting
# from the smallest subproblems up to the original problem.
#
# Approach:
#   1. Define the table and its meaning.
#   2. Initialize base cases.
#   3. Fill in the table using a recurrence relation.
#   4. Return the answer from the table.
#
# Advantages over memoization:
#   - No recursion overhead or stack overflow risk.
#   - Often easier to optimize space.
#
# Topics Covered:
#   - Fibonacci (tabulation)
#   - Climbing Stairs
#   - Coin Change (count ways + minimum coins)
#   - 0/1 Knapsack
#   - Longest Common Subsequence (LCS)
#   - Longest Increasing Subsequence (LIS)
# =============================================================

# ---------------------------------------------------------
# 1. Fibonacci — Tabulation
# ---------------------------------------------------------
print("=== Fibonacci — Tabulation ===")

def fib_table(n):
    """
    Compute nth Fibonacci number using a bottom-up table.

    Time:  O(n)
    Space: O(n)  [can be reduced to O(1) — see fib_optimized]
    """
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fib_optimized(n):
    """
    Fibonacci with O(1) space — keep only last two values.

    Time:  O(n)
    Space: O(1)
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print("Table (O(n) space):")
print(f"  {[fib_table(i) for i in range(10)]}")
print("Optimized (O(1) space):")
print(f"  {[fib_optimized(i) for i in range(10)]}")

# ---------------------------------------------------------
# 2. Climbing Stairs — Tabulation
# ---------------------------------------------------------
print("\n=== Climbing Stairs — Tabulation ===")

def climb_stairs(n):
    """
    Number of ways to climb n stairs (1 or 2 steps at a time).

    Time:  O(n)
    Space: O(1)
    """
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


for i in range(1, 9):
    print(f"  climb({i}) = {climb_stairs(i)} ways")

# ---------------------------------------------------------
# 3. Coin Change — Minimum Coins (Tabulation)
# ---------------------------------------------------------
print("\n=== Coin Change — Minimum Coins ===")

def coin_change_min(coins, amount):
    """
    Minimum coins to make up 'amount'.

    dp[i] = minimum coins needed to make amount i.

    Time:  O(amount * len(coins))
    Space: O(amount)
    """
    INF = float('inf')
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for amt in range(1, amount + 1):
        for coin in coins:
            if coin <= amt and dp[amt - coin] + 1 < dp[amt]:
                dp[amt] = dp[amt - coin] + 1

    return dp[amount] if dp[amount] != INF else -1


coins = [1, 5, 10, 25]
for amt in [0, 11, 30, 41]:
    print(f"  min_coins({coins}, {amt}) = {coin_change_min(coins, amt)}")

# ---------------------------------------------------------
# 4. Coin Change — Number of Ways (Tabulation)
# ---------------------------------------------------------
print("\n=== Coin Change — Count Ways ===")

def coin_change_ways(coins, amount):
    """
    Number of ways to make up 'amount' using given coins.

    dp[i] = number of ways to make amount i.

    Time:  O(amount * len(coins))
    Space: O(amount)
    """
    dp = [0] * (amount + 1)
    dp[0] = 1   # one way to make 0: use no coins

    for coin in coins:
        for amt in range(coin, amount + 1):
            dp[amt] += dp[amt - coin]

    return dp[amount]


for amt in [0, 5, 10, 11]:
    print(f"  ways({coins}, {amt}) = {coin_change_ways(coins, amt)}")

# ---------------------------------------------------------
# 5. 0/1 Knapsack — Tabulation
# ---------------------------------------------------------
print("\n=== 0/1 Knapsack — Tabulation ===")

def knapsack(weights, values, capacity):
    """
    0/1 Knapsack using a 2D DP table.

    dp[i][w] = max value using items 0..i-1 with weight limit w.

    Time:  O(n * capacity)
    Space: O(n * capacity)  [can be reduced to O(capacity) with 1D table]
    """
    n = len(weights)
    # (n+1) x (capacity+1) table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i-1
            dp[i][w] = dp[i - 1][w]
            # Take item i-1 (if it fits)
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               values[i - 1] + dp[i - 1][w - weights[i - 1]])

    return dp[n][capacity]


def knapsack_1d(weights, values, capacity):
    """
    Space-optimized 0/1 Knapsack with O(capacity) space.
    (Iterate weights in reverse to avoid using item twice.)
    """
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    return dp[capacity]


w = [1, 2, 3, 5]
v = [1, 6, 10, 16]
c = 7
print(f"  weights={w}, values={v}, capacity={c}")
print(f"  2D table:    max value = {knapsack(w, v, c)}")
print(f"  1D optimized: max value = {knapsack_1d(w, v, c)}")

# ---------------------------------------------------------
# 6. Longest Common Subsequence — Tabulation
# ---------------------------------------------------------
print("\n=== Longest Common Subsequence (LCS) ===")

def lcs(s1, s2):
    """
    Length of the LCS and reconstruct the subsequence.

    dp[i][j] = length of LCS of s1[:i] and s2[:j]

    Time:  O(m * n)
    Space: O(m * n)
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS string
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str.append(s1[i - 1])
            i -= 1; j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], "".join(reversed(lcs_str))


for s1, s2 in [("ABCBDAB", "BDCAB"), ("AGGTAB", "GXTXAYB")]:
    length, subseq = lcs(s1, s2)
    print(f"  LCS('{s1}', '{s2}') = '{subseq}' (length {length})")

# ---------------------------------------------------------
# 7. Longest Increasing Subsequence (LIS)
# ---------------------------------------------------------
print("\n=== Longest Increasing Subsequence (LIS) ===")

def lis(nums):
    """
    Length of the longest strictly increasing subsequence.

    dp[i] = length of LIS ending at index i.

    Time:  O(n²)
    Space: O(n)
    """
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


sequences = [
    [10, 9, 2, 5, 3, 7, 101, 18],
    [0, 1, 0, 3, 2, 3],
    [7, 7, 7, 7, 7],
]
for seq in sequences:
    print(f"  LIS({seq}) = {lis(seq)}")
