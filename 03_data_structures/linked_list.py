# =============================================================
# Module 3: Linked List Data Structure
# =============================================================
# A Linked List is a linear data structure where each element
# (node) contains a value and a pointer to the next node.
#
# Types covered:
#   - Singly Linked List
#   - Doubly Linked List
#
# Singly Linked List operations:
#   append(val)       — Add at tail          O(n)
#   prepend(val)      — Add at head          O(1)
#   insert(val, pos)  — Insert at position   O(n)
#   delete(val)       — Remove first match   O(n)
#   search(val)       — Find a value         O(n)
#   reverse()         — Reverse in-place     O(n)
# =============================================================

# ---------------------------------------------------------
# Node class (building block)
# ---------------------------------------------------------
class Node:
    """A single node in a linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


# ---------------------------------------------------------
# Singly Linked List
# ---------------------------------------------------------
print("=== Singly Linked List ===")

class SinglyLinkedList:
    """Singly linked list with common operations."""

    def __init__(self):
        self.head = None
        self._size = 0

    # --- Basic operations ---

    def append(self, value):
        """Add a node at the tail."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, value):
        """Add a node at the head (O(1))."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def insert(self, value, position):
        """Insert value at the given 0-indexed position."""
        if position < 0 or position > self._size:
            raise IndexError(f"Position {position} out of range (size={self._size})")
        if position == 0:
            self.prepend(value)
            return
        new_node = Node(value)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def delete(self, value):
        """Remove the first node with the given value. Returns True if found."""
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False

    def search(self, value):
        """Return the 0-indexed position of value, or -1 if not found."""
        current = self.head
        idx = 0
        while current:
            if current.value == value:
                return idx
            current = current.next
            idx += 1
        return -1

    def reverse(self):
        """Reverse the linked list in-place."""
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # --- Utility ---

    def to_list(self):
        """Return all values as a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self):
        return self._size

    def __str__(self):
        return " → ".join(str(v) for v in self.to_list()) + " → None"


sll = SinglyLinkedList()
print(f"Empty list: {sll}")

for val in [10, 20, 30, 40]:
    sll.append(val)
print(f"After appending 10,20,30,40: {sll}")

sll.prepend(5)
print(f"After prepend(5): {sll}")

sll.insert(25, 3)
print(f"After insert(25, pos=3): {sll}")

print(f"\nSearch 30: position {sll.search(30)}")
print(f"Search 99: position {sll.search(99)}")

sll.delete(25)
print(f"After delete(25): {sll}")

sll.reverse()
print(f"After reverse: {sll}")

# ---------------------------------------------------------
# Doubly Linked List
# ---------------------------------------------------------
print("\n=== Doubly Linked List ===")

class DNode:
    """Node for a doubly linked list."""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Doubly linked list — O(1) head/tail operations."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        """Add node at the tail."""
        node = DNode(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._size += 1

    def prepend(self, value):
        """Add node at the head."""
        node = DNode(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1

    def delete(self, value):
        """Remove first node with given value."""
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self._size -= 1
                return True
            current = current.next
        return False

    def to_list_forward(self):
        result, current = [], self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def to_list_backward(self):
        result, current = [], self.tail
        while current:
            result.append(current.value)
            current = current.prev
        return result

    def __len__(self):
        return self._size

    def __str__(self):
        return "None ↔ " + " ↔ ".join(str(v) for v in self.to_list_forward()) + " ↔ None"


dll = DoublyLinkedList()
for v in [1, 2, 3, 4, 5]:
    dll.append(v)
print(f"After appending 1-5: {dll}")

dll.prepend(0)
print(f"After prepend(0): {dll}")
print(f"Forward:  {dll.to_list_forward()}")
print(f"Backward: {dll.to_list_backward()}")

dll.delete(3)
print(f"After delete(3): {dll}")

# ---------------------------------------------------------
# Application: Detect Cycle in a Linked List (Floyd's algorithm)
# ---------------------------------------------------------
print("\n=== Application: Detect Cycle (Floyd's Algorithm) ===")

def has_cycle(head):
    """
    Detect a cycle using the two-pointer (tortoise & hare) technique.

    Time:  O(n)
    Space: O(1)
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# No cycle
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.next, n2.next, n3.next = n2, n3, n4
print(f"Linear list (no cycle): has_cycle = {has_cycle(n1)}")

# With cycle: n4 → n2
n4.next = n2
print(f"List with cycle:        has_cycle = {has_cycle(n1)}")
