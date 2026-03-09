# =============================================================
# Module 3: Queue Data Structure
# =============================================================
# A Queue is a FIFO (First-In, First-Out) data structure.
#
# Core operations:
#   enqueue(item) — Add item to the back           O(1) amortized
#   dequeue()     — Remove and return front item   O(1)
#   peek()        — View front item                O(1)
#   is_empty()    — Check if queue is empty        O(1)
#   size()        — Number of items                O(1)
#
# Applications:
#   - Task/job scheduling
#   - BFS (Breadth-First Search)
#   - Print queues
#   - Rate limiting
# =============================================================

from collections import deque

# ---------------------------------------------------------
# Implementation 1: Queue using collections.deque
# ---------------------------------------------------------
print("=== Queue Implementation (using deque) ===")

class Queue:
    """FIFO queue using collections.deque for O(1) operations."""

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """Add item to the back of the queue."""
        self._data.append(item)

    def dequeue(self):
        """Remove and return the front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._data.popleft()

    def peek(self):
        """Return front item without removing it."""
        if self.is_empty():
            raise IndexError("peek at an empty queue")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __str__(self):
        return f"Queue({list(self._data)})"


q = Queue()
print(f"Empty queue: {q}, is_empty={q.is_empty()}")

for item in ["A", "B", "C", "D"]:
    q.enqueue(item)
    print(f"  enqueued '{item}' → {q}")

print(f"\npeek: {q.peek()}")
print(f"size: {q.size()}")

while not q.is_empty():
    print(f"  dequeued '{q.dequeue()}' → {q}")

# ---------------------------------------------------------
# Implementation 2: Circular Queue (fixed capacity)
# ---------------------------------------------------------
print("\n=== Circular Queue (fixed capacity) ===")

class CircularQueue:
    """Fixed-size circular queue using a list."""

    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [None] * capacity
        self._head = 0
        self._tail = 0
        self._size = 0

    def enqueue(self, item):
        if self._size == self._capacity:
            raise OverflowError("Queue is full")
        self._data[self._tail] = item
        self._tail = (self._tail + 1) % self._capacity
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        item = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty queue")
        return self._data[self._head]

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def size(self):
        return self._size

    def __str__(self):
        items = [self._data[(self._head + i) % self._capacity]
                 for i in range(self._size)]
        return f"CircularQueue(cap={self._capacity}, items={items})"


cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq)

print(f"Dequeue: {cq.dequeue()}")
cq.enqueue(4)
print(cq)

try:
    cq.enqueue(5)
except OverflowError as e:
    print(f"Error: {e}")

# ---------------------------------------------------------
# Implementation 3: Priority Queue
# ---------------------------------------------------------
print("\n=== Priority Queue ===")

import heapq

class PriorityQueue:
    """Min-heap priority queue (lower number = higher priority)."""

    def __init__(self):
        self._heap = []
        self._index = 0     # tie-breaker for equal priorities

    def enqueue(self, item, priority):
        """Add item with given priority (lower = higher priority)."""
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1

    def dequeue(self):
        """Remove and return the highest-priority item."""
        if self.is_empty():
            raise IndexError("dequeue from an empty priority queue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at an empty priority queue")
        return self._heap[0][2]

    def is_empty(self):
        return len(self._heap) == 0

    def size(self):
        return len(self._heap)


pq = PriorityQueue()
tasks = [
    ("send email",    3),
    ("fix bug",       1),   # highest priority
    ("write tests",   2),
    ("update docs",   4),
    ("deploy",        2),
]

for task, priority in tasks:
    pq.enqueue(task, priority)
    print(f"  Added [{priority}] {task!r}")

print("\nProcessing tasks (by priority):")
while not pq.is_empty():
    print(f"  Processing: {pq.dequeue()!r}")

# ---------------------------------------------------------
# Application: BFS Level-Order Traversal
# ---------------------------------------------------------
print("\n=== Application: BFS using Queue ===")

def bfs(graph, start):
    """
    Breadth-First Search using a queue.

    Args:
        graph (dict): Adjacency list {node: [neighbours]}.
        start: Starting node.

    Returns:
        list: Nodes visited in BFS order.
    """
    visited = set()
    order = []
    q = Queue()
    q.enqueue(start)
    visited.add(start)

    while not q.is_empty():
        node = q.dequeue()
        order.append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                q.enqueue(neighbour)

    return order


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

result = bfs(graph, "A")
print(f"BFS from A: {result}")
