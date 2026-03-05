# =============================================================
# Practice Problems — Mixed Set
# =============================================================
# This file contains a mix of interview-style problems covering:
#   - Strings
#   - Arrays
#   - Linked Lists
#   - Trees
#   - Dynamic Programming
#   - Math
#
# Each problem includes:
#   - Problem statement
#   - Approach / intuition
#   - Solution
#   - Test cases
# =============================================================

from collections import defaultdict, Counter, deque


# =============================================================
# Problem 1: Two Sum
# =============================================================
# Given a list of integers and a target, find indices of two
# numbers that add up to the target.
#
# Approach: Use a hash map to store {value: index} seen so far.
# For each element, check if (target - element) is in the map.
#
# Time: O(n), Space: O(n)
# =============================================================

def two_sum(nums, target):
    """Return indices of the two numbers that sum to target."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


print("=== Problem 1: Two Sum ===")
tests = [
    ([2, 7, 11, 15], 9,  [0, 1]),
    ([3, 2, 4],      6,  [1, 2]),
    ([3, 3],         6,  [0, 1]),
]
for nums, target, expected in tests:
    result = two_sum(nums, target)
    status = "✓" if result == expected else "✗"
    print(f"  {status} two_sum({nums}, {target}) = {result}")


# =============================================================
# Problem 2: Valid Palindrome
# =============================================================
# A string is a palindrome if it reads the same forward and
# backward (ignoring non-alphanumeric chars and case).
#
# Approach: Two pointers from both ends.
#
# Time: O(n), Space: O(1)
# =============================================================

def is_palindrome(s):
    """Return True if s is a valid palindrome."""
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


print("\n=== Problem 2: Valid Palindrome ===")
palindrome_tests = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car",                      False),
    ("",                                True),
    ("Was it a car or a cat I saw?",    True),
]
for s, expected in palindrome_tests:
    result = is_palindrome(s)
    status = "✓" if result == expected else "✗"
    print(f"  {status} is_palindrome('{s[:30]}...') = {result}")


# =============================================================
# Problem 3: Maximum Profit (Buy and Sell Stock)
# =============================================================
# Find the maximum profit from a single buy/sell transaction.
#
# Approach: Track minimum price seen so far; update max profit.
#
# Time: O(n), Space: O(1)
# =============================================================

def max_profit(prices):
    """Return maximum profit from one buy-sell transaction."""
    if len(prices) < 2:
        return 0
    min_price = float('inf')
    max_prof = 0
    for price in prices:
        min_price = min(min_price, price)
        max_prof = max(max_prof, price - min_price)
    return max_prof


print("\n=== Problem 3: Max Stock Profit ===")
stock_tests = [
    ([7, 1, 5, 3, 6, 4],  5),
    ([7, 6, 4, 3, 1],     0),
    ([1, 2],              1),
]
for prices, expected in stock_tests:
    result = max_profit(prices)
    status = "✓" if result == expected else "✗"
    print(f"  {status} max_profit({prices}) = {result}")


# =============================================================
# Problem 4: Group Anagrams
# =============================================================
# Group a list of strings by their anagram equivalence class.
#
# Approach: Sort each word → use as a key in a dict.
#
# Time: O(n * k log k) where k = max word length
# Space: O(n * k)
# =============================================================

def group_anagrams(words):
    """Group words that are anagrams of each other."""
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())


print("\n=== Problem 4: Group Anagrams ===")
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = group_anagrams(words)
print(f"  Input: {words}")
print(f"  Groups:")
for g in sorted(groups, key=len, reverse=True):
    print(f"    {sorted(g)}")


# =============================================================
# Problem 5: Longest Substring Without Repeating Characters
# =============================================================
# Find the length of the longest substring with all unique chars.
#
# Approach: Sliding window with a set.
#
# Time: O(n), Space: O(k) where k = charset size
# =============================================================

def length_of_longest_substring(s):
    """Return length of longest substring without repeating chars."""
    char_index = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= left:
            left = char_index[ch] + 1
        char_index[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len


print("\n=== Problem 5: Longest Substring Without Repeating Chars ===")
substr_tests = [
    ("abcabcbb", 3),
    ("bbbbb",    1),
    ("pwwkew",   3),
    ("",         0),
]
for s, expected in substr_tests:
    result = length_of_longest_substring(s)
    status = "✓" if result == expected else "✗"
    print(f"  {status} longest_no_repeat('{s}') = {result}")


# =============================================================
# Problem 6: Number of Islands (BFS/DFS on Grid)
# =============================================================
# Count islands in a binary grid (1=land, 0=water).
# An island is a group of connected 1s (horizontally/vertically).
#
# Approach: DFS — mark visited cells as '0'.
#
# Time: O(m * n), Space: O(m * n) recursion stack
# =============================================================

def num_islands(grid):
    """Count number of islands in binary grid."""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'   # mark visited
        dfs(r + 1, c); dfs(r - 1, c)
        dfs(r, c + 1); dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count


print("\n=== Problem 6: Number of Islands ===")
grid1 = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0'],
]
grid2 = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1'],
]
print(f"  Grid 1 → {num_islands(grid1)} island(s) (expected 1)")
print(f"  Grid 2 → {num_islands(grid2)} island(s) (expected 3)")


# =============================================================
# Problem 7: Merge Intervals
# =============================================================
# Merge overlapping intervals.
#
# Approach: Sort by start, greedily extend the last merged interval.
#
# Time: O(n log n), Space: O(n)
# =============================================================

def merge_intervals(intervals):
    """Merge all overlapping intervals."""
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


print("\n=== Problem 7: Merge Intervals ===")
interval_tests = [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]],               [[1,5]]),
]
for intervals, expected in interval_tests:
    result = merge_intervals([i[:] for i in intervals])
    status = "✓" if result == expected else "✗"
    print(f"  {status} merge({intervals}) = {result}")


# =============================================================
# Problem 8: Valid Parentheses
# =============================================================
# Determine if brackets are balanced and properly nested.
#
# Time: O(n), Space: O(n)
# =============================================================

def is_valid_parens(s):
    """Return True if bracket expression is valid."""
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in mapping:
            top = stack.pop() if stack else '#'
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)
    return not stack


print("\n=== Problem 8: Valid Parentheses ===")
paren_tests = [
    ("()",        True),
    ("()[]{}",    True),
    ("(]",        False),
    ("([)]",      False),
    ("{[]}",      True),
]
for s, expected in paren_tests:
    result = is_valid_parens(s)
    status = "✓" if result == expected else "✗"
    print(f"  {status} valid_parens('{s}') = {result}")
