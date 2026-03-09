# =============================================================
# Module 4: Searching Algorithms
# =============================================================
# Topics Covered:
#   - Linear Search      O(n)
#   - Binary Search      O(log n) — iterative and recursive
#   - Jump Search        O(√n)
#   - Interpolation Search O(log log n) average case
# =============================================================

import math

# ---------------------------------------------------------
# 1. Linear Search
# ---------------------------------------------------------
print("=== Linear Search ===")

def linear_search(arr, target):
    """
    Search for target by scanning every element.

    Time:  O(n)
    Space: O(1)

    Returns:
        int: Index of target, or -1 if not found.
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


arr = [4, 2, 7, 1, 9, 3, 8, 5]
print(f"Array: {arr}")
for t in [7, 5, 10]:
    idx = linear_search(arr, t)
    print(f"  linear_search({t}) → index {idx}")

# ---------------------------------------------------------
# 2. Binary Search (requires sorted array)
# ---------------------------------------------------------
print("\n=== Binary Search ===")

def binary_search_iterative(arr, target):
    """
    Iterative binary search on a sorted array.

    Time:  O(log n)
    Space: O(1)

    Returns:
        int: Index of target, or -1 if not found.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2    # avoids overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive binary search.

    Time:  O(log n)
    Space: O(log n) — call stack
    """
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"Sorted array: {sorted_arr}")
for t in [7, 1, 19, 10]:
    i = binary_search_iterative(sorted_arr, t)
    r = binary_search_recursive(sorted_arr, t)
    print(f"  binary_search({t:>2}) → iterative={i:>2}, recursive={r:>2}")

# Find first/last occurrence in array with duplicates
def binary_search_first(arr, target):
    """Find index of first occurrence of target."""
    left, right, result = 0, len(arr) - 1, -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1     # keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def binary_search_last(arr, target):
    """Find index of last occurrence of target."""
    left, right, result = 0, len(arr) - 1, -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1      # keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


dup_arr = [1, 2, 2, 2, 3, 4, 4, 5]
print(f"\nArray with duplicates: {dup_arr}")
print(f"  First occurrence of 2: {binary_search_first(dup_arr, 2)}")
print(f"  Last  occurrence of 2: {binary_search_last(dup_arr, 2)}")
print(f"  First occurrence of 4: {binary_search_first(dup_arr, 4)}")

# ---------------------------------------------------------
# 3. Jump Search
# ---------------------------------------------------------
print("\n=== Jump Search ===")

def jump_search(arr, target):
    """
    Search by jumping ahead by √n steps, then linear scan.

    Requires: sorted array
    Time:  O(√n)
    Space: O(1)
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jump ahead until we overshoot
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear scan in the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
        if arr[i] > target:
            return -1
    return -1


print(f"Sorted array: {sorted_arr}")
for t in [7, 1, 19, 10]:
    idx = jump_search(sorted_arr, t)
    print(f"  jump_search({t:>2}) → index {idx:>2}")

# ---------------------------------------------------------
# 4. Complexity Summary
# ---------------------------------------------------------
print("\n=== Complexity Summary ===")
print(f"{'Algorithm':<25} {'Best':<10} {'Average':<12} {'Worst':<12} {'Space'}")
print("-" * 65)
rows = [
    ("Linear Search",       "O(1)",     "O(n)",        "O(n)",       "O(1)"),
    ("Binary Search",       "O(1)",     "O(log n)",    "O(log n)",   "O(1)"),
    ("Binary Search (rec)", "O(1)",     "O(log n)",    "O(log n)",   "O(log n)"),
    ("Jump Search",         "O(1)",     "O(√n)",       "O(√n)",      "O(1)"),
]
for row in rows:
    print(f"  {row[0]:<23} {row[1]:<10} {row[2]:<12} {row[3]:<12} {row[4]}")
