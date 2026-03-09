# =============================================================
# Module 5: Classic Dynamic Programming Problems
# =============================================================
# This file contains well-known DP problems with clear
# explanations and optimized implementations.
#
# Problems:
#   1. House Robber
#   2. Maximum Subarray (Kadane's Algorithm)
#   3. Edit Distance (Levenshtein)
#   4. Longest Palindromic Subsequence
#   5. Matrix Chain Multiplication
#   6. Word Break
#   7. Unique Paths in a Grid
# =============================================================

# ---------------------------------------------------------
# 1. House Robber
# ---------------------------------------------------------
print("=== House Robber ===")

def house_robber(houses):
    """
    Rob houses (no two adjacent) to maximize money.

    dp[i] = max money robbing from houses[0..i]

    Recurrence: dp[i] = max(dp[i-1], dp[i-2] + houses[i])

    Time:  O(n)
    Space: O(1)
    """
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]

    prev2, prev1 = 0, 0
    for amount in houses:
        curr = max(prev1, prev2 + amount)
        prev2, prev1 = prev1, curr
    return prev1


examples = [
    ([1, 2, 3, 1],        4),
    ([2, 7, 9, 3, 1],     12),
    ([2, 1, 1, 2],         4),
    ([0],                  0),
]
for houses, expected in examples:
    result = house_robber(houses)
    status = "✓" if result == expected else "✗"
    print(f"  {status} houses={houses} → rob ${result}")

# ---------------------------------------------------------
# 2. Maximum Subarray — Kadane's Algorithm
# ---------------------------------------------------------
print("\n=== Maximum Subarray (Kadane's Algorithm) ===")

def max_subarray(nums):
    """
    Find the contiguous subarray with the maximum sum.

    Time:  O(n)
    Space: O(1)

    Returns:
        tuple: (max_sum, start_index, end_index)
    """
    max_sum = current_sum = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if current_sum + nums[i] < nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, start, end


test_arrays = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [1],
    [5, 4, -1, 7, 8],
    [-1, -2, -3, -4],
]
for arr in test_arrays:
    total, s, e = max_subarray(arr)
    print(f"  {arr}")
    print(f"    → max sum = {total}, subarray = {arr[s:e+1]}")

# ---------------------------------------------------------
# 3. Edit Distance (Levenshtein Distance)
# ---------------------------------------------------------
print("\n=== Edit Distance ===")

def edit_distance(word1, word2):
    """
    Minimum operations (insert, delete, replace) to convert
    word1 into word2.

    dp[i][j] = edit distance between word1[:i] and word2[:j]

    Time:  O(m * n)
    Space: O(m * n)
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i        # delete all chars from word1
    for j in range(n + 1):
        dp[0][j] = j        # insert all chars of word2

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]   # no operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],       # delete from word1
                    dp[i][j - 1],       # insert into word1
                    dp[i - 1][j - 1],   # replace
                )

    return dp[m][n]


pairs = [
    ("horse",   "ros",    3),
    ("intention","execution", 5),
    ("",        "abc",    3),
    ("abc",     "abc",    0),
]
for w1, w2, expected in pairs:
    dist = edit_distance(w1, w2)
    status = "✓" if dist == expected else "✗"
    print(f"  {status} edit_distance('{w1}', '{w2}') = {dist}")

# ---------------------------------------------------------
# 4. Longest Palindromic Subsequence
# ---------------------------------------------------------
print("\n=== Longest Palindromic Subsequence ===")

def longest_palindromic_subseq(s):
    """
    Length of longest subsequence of s that is a palindrome.

    LPS(s) = LCS(s, reverse(s))

    Time:  O(n²)
    Space: O(n²)
    """
    n = len(s)
    rev = s[::-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rev[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]


words = ["bbbab", "cbbd", "agbdba", "a", "aa"]
for w in words:
    print(f"  LPS('{w}') = {longest_palindromic_subseq(w)}")

# ---------------------------------------------------------
# 5. Word Break
# ---------------------------------------------------------
print("\n=== Word Break ===")

def word_break(s, word_dict):
    """
    Check if s can be segmented into words from word_dict.

    dp[i] = True if s[:i] can be segmented.

    Time:  O(n² * k) where k = avg word length
    Space: O(n)
    """
    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True    # empty string is always valid

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


dictionary = ["leet", "code", "apple", "pen", "applepen", "pine", "pineapple"]
tests = ["leetcode", "applepenapple", "catsandog", "pineapplepenapple"]
for s in tests:
    result = word_break(s, dictionary)
    print(f"  word_break('{s}') = {result}")

# ---------------------------------------------------------
# 6. Unique Paths in a Grid
# ---------------------------------------------------------
print("\n=== Unique Paths in a Grid ===")

def unique_paths(m, n):
    """
    Count unique paths from top-left to bottom-right of m×n grid
    (can only move right or down).

    dp[i][j] = number of ways to reach cell (i, j)

    Time:  O(m * n)
    Space: O(n) — only one row needed
    """
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[n - 1]


print(f"  unique_paths(3, 7) = {unique_paths(3, 7)}")
print(f"  unique_paths(3, 2) = {unique_paths(3, 2)}")
print(f"  unique_paths(1, 1) = {unique_paths(1, 1)}")

# With obstacles
def unique_paths_obstacles(grid):
    """
    Count paths where 1 = obstacle, 0 = free.
    """
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = 1 if grid[0][0] == 0 else 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]

    return dp[n - 1]


grid1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
grid2 = [[0, 1], [0, 0]]
print(f"\n  unique_paths with obstacle grid1 = {unique_paths_obstacles(grid1)}")
print(f"  unique_paths with obstacle grid2 = {unique_paths_obstacles(grid2)}")
