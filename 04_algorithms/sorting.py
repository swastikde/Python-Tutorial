# =============================================================
# Module 4: Sorting Algorithms
# =============================================================
# Topics Covered:
#   - Bubble Sort     O(n²)
#   - Selection Sort  O(n²)
#   - Insertion Sort  O(n²)
#   - Merge Sort      O(n log n)
#   - Quick Sort      O(n log n) average
#   - Heap Sort       O(n log n)
#   - Counting Sort   O(n + k)
# =============================================================

import random
import time

# Helper to verify sorting correctness
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


# ---------------------------------------------------------
# 1. Bubble Sort
# ---------------------------------------------------------
def bubble_sort(arr):
    """
    Repeatedly swap adjacent out-of-order elements.

    Time:  O(n²) worst/avg, O(n) best (already sorted)
    Space: O(1) in-place
    """
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:         # early exit: already sorted
            break
    return arr


# ---------------------------------------------------------
# 2. Selection Sort
# ---------------------------------------------------------
def selection_sort(arr):
    """
    Select the minimum element and place it at position i.

    Time:  O(n²) always
    Space: O(1) in-place
    """
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# ---------------------------------------------------------
# 3. Insertion Sort
# ---------------------------------------------------------
def insertion_sort(arr):
    """
    Build a sorted sub-array one element at a time.

    Time:  O(n²) worst, O(n) best (nearly sorted input)
    Space: O(1) in-place
    """
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ---------------------------------------------------------
# 4. Merge Sort
# ---------------------------------------------------------
def merge_sort(arr):
    """
    Divide array in half, sort each half, merge them.

    Time:  O(n log n) always
    Space: O(n) auxiliary
    """
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]


# ---------------------------------------------------------
# 5. Quick Sort
# ---------------------------------------------------------
def quick_sort(arr):
    """
    Partition around a pivot and recursively sort sub-arrays.

    Time:  O(n log n) average, O(n²) worst (bad pivot)
    Space: O(log n) average — call stack
    """
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr) // 2]   # median-of-three would be better
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# ---------------------------------------------------------
# 6. Heap Sort
# ---------------------------------------------------------
def heap_sort(arr):
    """
    Build a max-heap, then repeatedly extract the maximum.

    Time:  O(n log n) always
    Space: O(1) in-place
    """
    arr = arr[:]
    n = len(arr)

    def heapify(arr, n, i):
        largest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


# ---------------------------------------------------------
# 7. Counting Sort
# ---------------------------------------------------------
def counting_sort(arr, max_val=None):
    """
    Sort non-negative integers by counting occurrences.

    Time:  O(n + k)  where k = max value
    Space: O(k)
    """
    if not arr:
        return []
    k = max_val if max_val is not None else max(arr)
    count = [0] * (k + 1)
    for val in arr:
        count[val] += 1
    result = []
    for val, cnt in enumerate(count):
        result.extend([val] * cnt)
    return result


# ---------------------------------------------------------
# Test all algorithms
# ---------------------------------------------------------
print("=== Sorting Algorithms — Correctness Test ===")

test_data = [64, 25, 12, 22, 11, 90, 3, 45, 7]
print(f"Original: {test_data}")

algorithms = [
    ("Bubble Sort",    bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Merge Sort",     merge_sort),
    ("Quick Sort",     quick_sort),
    ("Heap Sort",      heap_sort),
    ("Counting Sort",  counting_sort),
]

for name, fn in algorithms:
    result = fn(test_data)
    status = "✓" if is_sorted(result) else "✗"
    print(f"  {status} {name:<18}: {result}")

# ---------------------------------------------------------
# Performance comparison
# ---------------------------------------------------------
print("\n=== Performance Comparison (n=2000) ===")

large = random.sample(range(10000), 2000)
print(f"{'Algorithm':<18} {'Time (ms)':>12}")
print("-" * 32)

for name, fn in algorithms:
    start = time.perf_counter()
    fn(large)
    elapsed = (time.perf_counter() - start) * 1000
    print(f"  {name:<16} {elapsed:>10.2f} ms")

# ---------------------------------------------------------
# Summary table
# ---------------------------------------------------------
print("\n=== Complexity Summary ===")
print(f"{'Algorithm':<18} {'Best':<12} {'Average':<12} {'Worst':<12} {'Space':<10} {'Stable'}")
print("-" * 70)
rows = [
    ("Bubble Sort",    "O(n)",     "O(n²)",    "O(n²)",    "O(1)",  "Yes"),
    ("Selection Sort", "O(n²)",    "O(n²)",    "O(n²)",    "O(1)",  "No"),
    ("Insertion Sort", "O(n)",     "O(n²)",    "O(n²)",    "O(1)",  "Yes"),
    ("Merge Sort",     "O(n logn)","O(n logn)","O(n logn)","O(n)",  "Yes"),
    ("Quick Sort",     "O(n logn)","O(n logn)","O(n²)",    "O(logn)","No"),
    ("Heap Sort",      "O(n logn)","O(n logn)","O(n logn)","O(1)",  "No"),
    ("Counting Sort",  "O(n+k)",   "O(n+k)",   "O(n+k)",   "O(k)",  "Yes"),
]
for row in rows:
    print(f"  {row[0]:<16} {row[1]:<12} {row[2]:<12} {row[3]:<12} {row[4]:<10} {row[5]}")
