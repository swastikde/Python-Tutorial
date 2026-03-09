# =============================================================
# Module 1: Joins in Python
# =============================================================
# Topics Covered:
#   - str.join()  — join a sequence of strings with a separator
#   - SQL-style data joins using Python dicts and lists
#       * INNER JOIN
#       * LEFT JOIN
#       * RIGHT JOIN
#       * FULL OUTER JOIN
#   - Set joins (union, intersection, difference,
#                symmetric difference)
# =============================================================

# ---------------------------------------------------------
# 1. str.join() — String Joining
# ---------------------------------------------------------
# Syntax: separator.join(iterable)
# The separator is inserted between every element of the
# iterable.  All elements must be strings.

print("=== str.join() ===")

words = ["Python", "is", "awesome"]

# Join with a space
sentence = " ".join(words)
print(f"Space join:   {sentence}")

# Join with a comma + space
csv_line = ", ".join(words)
print(f"CSV join:     {csv_line}")

# Join with no separator (concatenation)
concat = "".join(words)
print(f"Empty join:   {concat}")

# Join with a custom separator
path_parts = ["home", "user", "documents", "file.txt"]
file_path = "/".join(path_parts)
print(f"Path join:    {file_path}")

# Join a list of characters back into a string
chars = ["H", "e", "l", "l", "o"]
word = "".join(chars)
print(f"Char join:    {word}")

# Join with a newline separator
lines = ["Line 1", "Line 2", "Line 3"]
block = "\n".join(lines)
print(f"\nNewline join:\n{block}")

# ---------------------------------------------------------
# 2. str.join() — Common Patterns
# ---------------------------------------------------------
print("\n=== str.join() — Common Patterns ===")

# Convert non-string items first with map()
numbers = [1, 2, 3, 4, 5]
numbers_str = ", ".join(map(str, numbers))
print(f"Numbers joined:     {numbers_str}")

# Reverse a string using join + reversed()
original = "Python"
reversed_str = "".join(reversed(original))
print(f"Reversed 'Python':  {reversed_str}")

# Join only elements that satisfy a condition
mixed = ["apple", "", "banana", None, "cherry", ""]
valid = [item for item in mixed if item]   # filter falsy values
result = " | ".join(valid)
print(f"Filtered join:      {result}")

# Join lines from a generator (memory-efficient)
def generate_lines(n):
    for i in range(1, n + 1):
        yield f"item_{i}"

joined = ", ".join(generate_lines(5))
print(f"Generator join:     {joined}")

# ---------------------------------------------------------
# 3. SQL-style Data Joins in Pure Python
# ---------------------------------------------------------
# SQL joins operate on tables (rows sharing a common key).
# We model each table as a list of dicts.
#
# Example tables:
#   employees  — employee records with a dept_id foreign key
#   departments — department records with a dept_id primary key

print("\n=== SQL-style Data Joins ===")

employees = [
    {"emp_id": 1, "name": "Alice",   "dept_id": 10},
    {"emp_id": 2, "name": "Bob",     "dept_id": 20},
    {"emp_id": 3, "name": "Charlie", "dept_id": 10},
    {"emp_id": 4, "name": "Diana",   "dept_id": 30},
    {"emp_id": 5, "name": "Eve",     "dept_id": None},  # no dept
]

departments = [
    {"dept_id": 10, "dept_name": "Engineering"},
    {"dept_id": 20, "dept_name": "Marketing"},
    {"dept_id": 40, "dept_name": "Finance"},            # no employee
]

def _print_table(rows, cols):
    """Pretty-print a list of dicts as a table."""
    if not rows:
        print("  (no rows)")
        return
    widths = {col: max(len(col), max(len(str(r.get(col, ""))) for r in rows))
              for col in cols}
    header = " | ".join(f"{col:<{widths[col]}}" for col in cols)
    sep    = "-+-".join("-" * widths[col] for col in cols)
    print(f"  {header}")
    print(f"  {sep}")
    for row in rows:
        line = " | ".join(f"{str(row.get(col, '')):<{widths[col]}}" for col in cols)
        print(f"  {line}")

# ---------------------------------------------------------
# 3a. INNER JOIN
# ---------------------------------------------------------
# Returns rows where the key matches in BOTH tables.
# Employees without a department — and departments without
# any employee — are excluded.

print("\n--- INNER JOIN ---")
print("  (Only rows where dept_id matches in both tables)\n")

def inner_join(left, right, key):
    """
    INNER JOIN left and right tables on a shared key.

    Args:
        left  (list[dict]): Left table.
        right (list[dict]): Right table.
        key   (str):        Column name to join on.

    Returns:
        list[dict]: Merged rows where key matches in both tables.
    """
    # Build a lookup dict from the right table for O(1) access
    right_lookup = {}
    for row in right:
        k = row[key]
        right_lookup.setdefault(k, []).append(row)

    result = []
    for left_row in left:
        k = left_row[key]
        if k in right_lookup:
            for right_row in right_lookup[k]:
                merged = {**left_row, **right_row}
                result.append(merged)
    return result


inner = inner_join(employees, departments, key="dept_id")
cols  = ["emp_id", "name", "dept_id", "dept_name"]
_print_table(inner, cols)

# ---------------------------------------------------------
# 3b. LEFT JOIN (LEFT OUTER JOIN)
# ---------------------------------------------------------
# Returns ALL rows from the left table.
# Matching rows from the right table are merged in;
# non-matching rows get None for right-table columns.

print("\n--- LEFT JOIN ---")
print("  (All employees; NULL dept_name if no matching dept)\n")

def left_join(left, right, key):
    """
    LEFT OUTER JOIN left and right tables on a shared key.

    All rows from 'left' are included.  Where there is no
    matching row in 'right', right-side columns are None.

    Args:
        left  (list[dict]): Left table (all rows kept).
        right (list[dict]): Right table (matched or NULL).
        key   (str):        Column name to join on.

    Returns:
        list[dict]: Merged rows with all left rows present.
    """
    right_lookup = {}
    for row in right:
        k = row[key]
        right_lookup.setdefault(k, []).append(row)

    # Collect all right-table column names (excluding the key)
    right_cols = {col for row in right for col in row if col != key}

    result = []
    for left_row in left:
        k = left_row[key]
        if k in right_lookup:
            for right_row in right_lookup[k]:
                merged = {**left_row, **right_row}
                result.append(merged)
        else:
            # Pad missing right-side columns with None
            merged = {**left_row, **{col: None for col in right_cols}}
            result.append(merged)
    return result


left = left_join(employees, departments, key="dept_id")
_print_table(left, cols)

# ---------------------------------------------------------
# 3c. RIGHT JOIN (RIGHT OUTER JOIN)
# ---------------------------------------------------------
# Returns ALL rows from the right table.
# Matching rows from the left table are merged in;
# non-matching rows get None for left-table columns.

print("\n--- RIGHT JOIN ---")
print("  (All departments; NULL employee info if no matching emp)\n")

def right_join(left, right, key):
    """
    RIGHT OUTER JOIN left and right tables on a shared key.

    Equivalent to a LEFT JOIN with tables swapped.

    Args:
        left  (list[dict]): Left table (matched or NULL).
        right (list[dict]): Right table (all rows kept).
        key   (str):        Column name to join on.

    Returns:
        list[dict]: Merged rows with all right rows present.
    """
    return left_join(right, left, key)


right = right_join(employees, departments, key="dept_id")
_print_table(right, cols)

# ---------------------------------------------------------
# 3d. FULL OUTER JOIN
# ---------------------------------------------------------
# Returns ALL rows from BOTH tables.
# Where there is no match, the missing side is padded with None.

print("\n--- FULL OUTER JOIN ---")
print("  (All employees AND all departments; NULL where no match)\n")

def full_outer_join(left, right, key):
    """
    FULL OUTER JOIN left and right tables on a shared key.

    All rows from both tables are present in the result.
    Non-matching rows are padded with None on the missing side.

    Args:
        left  (list[dict]): Left table.
        right (list[dict]): Right table.
        key   (str):        Column name to join on.

    Returns:
        list[dict]: All rows from both tables, merged where possible.
    """
    left_result  = left_join(left, right, key)
    right_result = left_join(right, left, key)

    # Collect keys already covered by the left join
    left_keys = {row[key] for row in left}

    # Add right-only rows (those whose key has no match on the left)
    extra = [row for row in right_result if row[key] not in left_keys]
    return left_result + extra


full = full_outer_join(employees, departments, key="dept_id")
_print_table(full, cols)

# ---------------------------------------------------------
# 4. Set Joins (Set Operations)
# ---------------------------------------------------------
# Python sets support mathematical set operations that mirror
# relational JOIN concepts.

print("\n=== Set Joins (Set Operations) ===")

team_a = {"Alice", "Bob", "Charlie", "Diana"}
team_b = {"Charlie", "Diana", "Eve", "Frank"}

print(f"Team A: {sorted(team_a)}")
print(f"Team B: {sorted(team_b)}")

# UNION — all members from either team (like FULL OUTER JOIN)
union = team_a | team_b                          # or team_a.union(team_b)
print(f"\nUNION (A | B):                {sorted(union)}")

# INTERSECTION — members in both teams (like INNER JOIN)
intersection = team_a & team_b                   # or team_a.intersection(team_b)
print(f"INTERSECTION (A & B):         {sorted(intersection)}")

# DIFFERENCE — members in A but not B (like LEFT JOIN exclusive)
diff_a = team_a - team_b                         # or team_a.difference(team_b)
print(f"DIFFERENCE (A - B):           {sorted(diff_a)}")

# DIFFERENCE — members in B but not A (like RIGHT JOIN exclusive)
diff_b = team_b - team_a                         # or team_b.difference(team_a)
print(f"DIFFERENCE (B - A):           {sorted(diff_b)}")

# SYMMETRIC DIFFERENCE — members in either but not both
sym_diff = team_a ^ team_b                       # or team_a.symmetric_difference(team_b)
print(f"SYMMETRIC DIFFERENCE (A ^ B): {sorted(sym_diff)}")

# ---------------------------------------------------------
# 5. Practical Example — Join to Enrich a Dataset
# ---------------------------------------------------------
print("\n=== Practical Example: Enrich Orders with Product Info ===")

orders = [
    {"order_id": 101, "product_id": "P01", "qty": 2},
    {"order_id": 102, "product_id": "P03", "qty": 1},
    {"order_id": 103, "product_id": "P02", "qty": 5},
    {"order_id": 104, "product_id": "P99", "qty": 1},  # unknown product
]

products = [
    {"product_id": "P01", "product_name": "Laptop",  "price": 999.99},
    {"product_id": "P02", "product_name": "Mouse",   "price":  29.99},
    {"product_id": "P03", "product_name": "Keyboard", "price":  49.99},
]

enriched = left_join(orders, products, key="product_id")

print(f"\n  {'order_id':<10} {'product_id':<12} {'qty':<5} "
      f"{'product_name':<12} {'price':<8} {'total'}")
print("  " + "-" * 62)
for row in enriched:
    price  = row.get("price")
    qty    = row["qty"]
    total  = f"${price * qty:.2f}" if price is not None else "N/A"
    pname  = row.get("product_name") or "UNKNOWN"
    pstr   = f"${price:.2f}" if price is not None else "N/A"
    print(f"  {row['order_id']:<10} {row['product_id']:<12} {qty:<5} "
          f"{pname:<12} {pstr:<8} {total}")
