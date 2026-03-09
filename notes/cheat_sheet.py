# =============================================================
# Python Mastery — Cheat Sheet & Quick Reference
# =============================================================
# This file contains concise summaries of key concepts across
# all modules in this repository.
# =============================================================

# ─────────────────────────────────────────────────────────────
# 1. PYTHON BASICS
# ─────────────────────────────────────────────────────────────

BASICS = """
DATA TYPES
  int, float, complex, str, bool, None
  list, tuple, dict, set, frozenset

TYPE CONVERSION
  int(), float(), str(), bool(), list(), tuple(), set()

OPERATORS
  Arithmetic:   + - * / // % **
  Comparison:   == != < > <= >=
  Logical:      and  or  not
  Bitwise:      & | ^ ~ << >>
  Identity:     is  is not
  Membership:   in  not in

CONDITIONALS
  if cond:
      ...
  elif cond:
      ...
  else:
      ...

  # Ternary
  val = x if cond else y

LOOPS
  for item in iterable: ...
  for i in range(start, stop, step): ...
  while cond: ...
  break / continue / pass

  # else on loops — runs if no break
  for ... :
      ...
  else:
      # runs when loop completes without break

COMPREHENSIONS
  [expr for x in iterable if cond]
  {key: val for x in iterable}
  {expr for x in iterable}

FUNCTIONS
  def func(a, b=default, *args, **kwargs): ...
  lambda x: x * 2
"""

# ─────────────────────────────────────────────────────────────
# 2. OOP
# ─────────────────────────────────────────────────────────────

OOP = """
CLASS DEFINITION
  class MyClass:
      class_attr = value                    # shared by all instances

      def __init__(self, x):
          self.x = x                        # instance attribute

      def method(self): ...                 # instance method
      @classmethod
      def cls_method(cls): ...              # class method
      @staticmethod
      def static_method(): ...              # static method

ACCESS CONTROL (by convention)
  self.x     → public
  self._x    → protected (don't touch from outside)
  self.__x   → private (name-mangled to _ClassName__x)

PROPERTY
  @property
  def value(self): return self._value
  @value.setter
  def value(self, v): self._value = v

INHERITANCE
  class Child(Parent):
      def __init__(self):
          super().__init__()

ABSTRACT CLASS
  from abc import ABC, abstractmethod
  class Base(ABC):
      @abstractmethod
      def method(self): pass

KEY DUNDER METHODS
  __init__    constructor
  __str__     str() / print()
  __repr__    repr() / debugging
  __len__     len()
  __eq__      ==
  __lt__      <
  __add__     +
  __iter__    for ... in
  __getitem__ obj[key]
"""

# ─────────────────────────────────────────────────────────────
# 3. DATA STRUCTURES — COMPLEXITY
# ─────────────────────────────────────────────────────────────

DS_COMPLEXITY = """
LIST (Dynamic Array)
  Access:   O(1)  | Search: O(n)
  Append:   O(1)* | Insert: O(n)
  Delete:   O(n)  | Sort:   O(n log n)

DICT (Hash Table)
  Get/Set/Delete: O(1) average, O(n) worst

SET (Hash Table)
  Add/Remove/In: O(1) average

STACK (via list or deque)
  push / pop / peek: O(1)

QUEUE (via deque)
  enqueue / dequeue: O(1)

LINKED LIST (Singly)
  Prepend:    O(1)
  Append:     O(n)
  Search:     O(n)
  Delete:     O(n)

BINARY SEARCH TREE
  Search / Insert / Delete: O(log n) avg, O(n) worst

HEAP (via heapq)
  Push / Pop: O(log n)
  Peek min:   O(1)
  Build heap: O(n)

GRAPH (Adjacency List)
  Add vertex/edge: O(1)
  DFS / BFS:       O(V + E)
"""

# ─────────────────────────────────────────────────────────────
# 4. ALGORITHMS — COMPLEXITY
# ─────────────────────────────────────────────────────────────

ALGO_COMPLEXITY = """
SORTING
  Bubble / Selection / Insertion:  O(n²)
  Merge Sort:                      O(n log n)  stable
  Quick Sort:                      O(n log n) avg, O(n²) worst
  Heap Sort:                       O(n log n)
  Counting / Radix Sort:           O(n + k)

SEARCHING
  Linear Search:  O(n)
  Binary Search:  O(log n)  — requires sorted array
  Jump Search:    O(√n)     — requires sorted array

GRAPH ALGORITHMS
  BFS / DFS:                  O(V + E)
  Dijkstra (min-heap):        O((V + E) log V)
  Bellman-Ford:               O(V * E)
  Topological Sort (Kahn's):  O(V + E)

DYNAMIC PROGRAMMING
  Most DP problems: O(n * m) time and space
  Space optimization with 1D arrays: O(m) or O(n)
"""

# ─────────────────────────────────────────────────────────────
# 5. DP PATTERNS
# ─────────────────────────────────────────────────────────────

DP_PATTERNS = """
FIBONACCI / STAIRCASE
  dp[i] = dp[i-1] + dp[i-2]

UNBOUNDED KNAPSACK (item can be reused)
  for coin in coins:
      for amt in range(coin, target+1):
          dp[amt] += dp[amt - coin]

0/1 KNAPSACK (item used at most once)
  for i in range(n):
      for w in range(capacity, weights[i]-1, -1):
          dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

LONGEST COMMON SUBSEQUENCE (LCS)
  if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
  else:                   dp[i][j] = max(dp[i-1][j], dp[i][j-1])

EDIT DISTANCE
  if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]
  else: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

INTERVAL DP
  for length in range(2, n+1):
      for i in range(n - length + 1):
          j = i + length - 1
          dp[i][j] = min/max over k in [i, j-1]
"""

# ─────────────────────────────────────────────────────────────
# 6. PYTHON STANDARD LIBRARY — USEFUL MODULES
# ─────────────────────────────────────────────────────────────

STDLIB = """
collections
  deque            → O(1) append/pop from both ends
  Counter          → count occurrences: Counter("hello")
  defaultdict      → dict with default factory
  OrderedDict      → dict that remembers insertion order
  namedtuple       → tuple with named fields

heapq
  heappush(heap, item)
  heappop(heap)        → min element
  heapify(list)        → convert list to heap in O(n)
  nlargest(n, iterable)
  nsmallest(n, iterable)

itertools
  combinations(iterable, r)
  permutations(iterable, r)
  product(*iterables)
  chain(*iterables)
  groupby(iterable, key)

functools
  lru_cache(maxsize=None)    → memoization decorator
  reduce(func, iterable)
  partial(func, *args)

math
  math.gcd(a, b)
  math.lcm(a, b)
  math.sqrt(x)
  math.ceil(x) / math.floor(x)
  math.inf  / float('inf')
  math.log(x, base)

bisect
  bisect_left(arr, x)   → insertion point (left)
  bisect_right(arr, x)  → insertion point (right)
  insort(arr, x)        → insert into sorted list O(n)
"""

# ─────────────────────────────────────────────────────────────
# 7. BIG-O NOTATION REMINDER
# ─────────────────────────────────────────────────────────────

BIG_O = """
Notation     Name             Example
─────────────────────────────────────────
O(1)         Constant         Hash table lookup
O(log n)     Logarithmic      Binary search
O(n)         Linear           Linear scan
O(n log n)   Linearithmic     Merge sort
O(n²)        Quadratic        Bubble sort
O(2ⁿ)        Exponential      All subsets (backtracking)
O(n!)        Factorial        All permutations

Tips:
  - Nested loops → multiply the complexities
  - Half the input each step → O(log n)
  - Process every element at each level → O(n log n)
"""

if __name__ == "__main__":
    sections = [
        ("1. Python Basics",        BASICS),
        ("2. OOP",                   OOP),
        ("3. Data Structures",       DS_COMPLEXITY),
        ("4. Algorithms",            ALGO_COMPLEXITY),
        ("5. DP Patterns",           DP_PATTERNS),
        ("6. Standard Library",      STDLIB),
        ("7. Big-O Notation",        BIG_O),
    ]
    for title, content in sections:
        print(f"\n{'='*60}")
        print(f"  {title}")
        print('='*60)
        print(content)
