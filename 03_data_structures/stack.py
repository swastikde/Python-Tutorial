# =============================================================
# Module 3: Stack Data Structure
# =============================================================
# A Stack is a LIFO (Last-In, First-Out) data structure.
#
# Core operations:
#   push(item)  — Add item to the top          O(1)
#   pop()       — Remove and return top item   O(1)
#   peek()      — View top item without removing O(1)
#   is_empty()  — Check if stack is empty      O(1)
#   size()      — Number of items in stack     O(1)
#
# Applications:
#   - Undo/redo in editors
#   - Function call stack
#   - Expression evaluation
#   - Balanced parentheses checking
# =============================================================

# ---------------------------------------------------------
# Implementation 1: Stack using a Python list
# ---------------------------------------------------------
print("=== Stack Implementation (using list) ===")

class Stack:
    """LIFO stack implemented on top of a Python list."""

    def __init__(self):
        self._data = []

    def push(self, item):
        """Add item to the top of the stack."""
        self._data.append(item)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._data.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek at an empty stack")
        return self._data[-1]

    def is_empty(self):
        """Return True if the stack has no items."""
        return len(self._data) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._data)

    def __str__(self):
        return f"Stack({self._data})"

    def __repr__(self):
        return self.__str__()


s = Stack()
print(f"Empty stack: {s}, is_empty={s.is_empty()}")

for val in [10, 20, 30, 40]:
    s.push(val)
    print(f"  pushed {val} → {s}")

print(f"\npeek: {s.peek()}")
print(f"size: {s.size()}")

while not s.is_empty():
    print(f"  popped {s.pop()} → {s}")

try:
    s.pop()
except IndexError as e:
    print(f"\nError: {e}")

# ---------------------------------------------------------
# Application 1: Balanced Parentheses Checker
# ---------------------------------------------------------
print("\n=== Application: Balanced Parentheses ===")

def is_balanced(expression):
    """
    Check whether an expression has balanced brackets.

    Args:
        expression (str): Expression to check.

    Returns:
        bool: True if brackets are balanced, False otherwise.

    Examples:
        >>> is_balanced("(a + b) * [c - {d}]")
        True
        >>> is_balanced("((a + b)")
        False
    """
    stack = Stack()
    matching = {')': '(', ']': '[', '}': '{'}
    openers = set(matching.values())

    for ch in expression:
        if ch in openers:
            stack.push(ch)
        elif ch in matching:
            if stack.is_empty() or stack.pop() != matching[ch]:
                return False

    return stack.is_empty()


test_cases = [
    ("(a + b) * [c - {d}]", True),
    ("((a + b)",             False),
    ("{[()]}",               True),
    ("{[(])}",               False),
    ("",                     True),
    ("(((",                  False),
]

for expr, expected in test_cases:
    result = is_balanced(expr)
    status = "✓" if result == expected else "✗"
    print(f"  {status} is_balanced({expr!r:<25}) = {result}")

# ---------------------------------------------------------
# Application 2: Evaluate Reverse Polish Notation (RPN)
# ---------------------------------------------------------
print("\n=== Application: Evaluate RPN Expressions ===")

def eval_rpn(tokens):
    """
    Evaluate a Reverse Polish Notation expression.

    Args:
        tokens (list[str]): Tokenized RPN expression.

    Returns:
        float: Result of the expression.

    Example:
        eval_rpn(["2", "3", "+", "4", "*"]) → 20  # (2+3)*4
    """
    stack = Stack()
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    for token in tokens:
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            stack.push(ops[token](a, b))
        else:
            stack.push(float(token))

    return stack.pop()


rpn_tests = [
    (["2", "3", "+"],                   5.0),    # 2+3
    (["2", "3", "+", "4", "*"],        20.0),    # (2+3)*4
    (["5", "1", "2", "+", "4", "*", "+", "3", "-"],  14.0),  # 5+((1+2)*4)-3
]

for tokens, expected in rpn_tests:
    result = eval_rpn(tokens)
    status = "✓" if result == expected else "✗"
    print(f"  {status} eval_rpn({tokens}) = {result}")

# ---------------------------------------------------------
# Application 3: Undo / Redo Simulation
# ---------------------------------------------------------
print("\n=== Application: Undo / Redo ===")

class TextEditor:
    """Simple text editor with undo/redo using two stacks."""

    def __init__(self):
        self._text = ""
        self._undo_stack = Stack()
        self._redo_stack = Stack()

    def type(self, chars):
        """Append characters to the text."""
        self._undo_stack.push(self._text)
        self._redo_stack = Stack()      # clear redo history on new action
        self._text += chars
        print(f"  Typed '{chars}' → text='{self._text}'")

    def undo(self):
        """Undo the last action."""
        if self._undo_stack.is_empty():
            print("  Nothing to undo.")
            return
        self._redo_stack.push(self._text)
        self._text = self._undo_stack.pop()
        print(f"  Undo → text='{self._text}'")

    def redo(self):
        """Redo the last undone action."""
        if self._redo_stack.is_empty():
            print("  Nothing to redo.")
            return
        self._undo_stack.push(self._text)
        self._text = self._redo_stack.pop()
        print(f"  Redo → text='{self._text}'")


editor = TextEditor()
editor.type("Hello")
editor.type(", ")
editor.type("World")
editor.undo()
editor.undo()
editor.redo()
editor.type("Python!")
editor.undo()
