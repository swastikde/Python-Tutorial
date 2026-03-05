# =============================================================
# Module 4: Backtracking Algorithms
# =============================================================
# Backtracking is an algorithmic technique that builds a
# solution incrementally, abandoning (backtracking) as soon
# as it determines the current path cannot lead to a valid
# solution.
#
# Pattern:
#   1. Choose: make a choice (add element to partial solution)
#   2. Explore: recurse with the choice made
#   3. Undo: remove the choice (backtrack) before trying the next
#
# Topics Covered:
#   - N-Queens Problem
#   - Sudoku Solver
#   - Generating all permutations
#   - Generating all subsets (power set)
#   - Word search in a grid
# =============================================================

# ---------------------------------------------------------
# 1. Generate All Permutations
# ---------------------------------------------------------
print("=== All Permutations ===")

def permutations(nums):
    """
    Generate all permutations of nums using backtracking.

    Time:  O(n! * n)
    Space: O(n) recursion depth
    """
    result = []

    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return
        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()

    backtrack([], nums)
    return result


perms = permutations([1, 2, 3])
print(f"permutations([1, 2, 3]): {len(perms)} total")
for p in perms:
    print(f"  {p}")

# ---------------------------------------------------------
# 2. Generate All Subsets (Power Set)
# ---------------------------------------------------------
print("\n=== All Subsets (Power Set) ===")

def subsets(nums):
    """
    Generate all subsets of nums (power set).

    Time:  O(2^n * n)
    Space: O(n)
    """
    result = []

    def backtrack(start, current):
        result.append(current[:])   # include current subset (even empty)
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


subs = subsets([1, 2, 3])
print(f"subsets([1, 2, 3]): {len(subs)} subsets")
for s in sorted(subs, key=len):
    print(f"  {s}")

# ---------------------------------------------------------
# 3. N-Queens Problem
# ---------------------------------------------------------
print("\n=== N-Queens Problem ===")

def solve_n_queens(n):
    """
    Place n queens on an n×n chessboard so no two queens
    attack each other.

    Returns:
        list[list[str]]: All valid board configurations.
    """
    solutions = []
    queens = []         # queens[row] = column index of queen in that row

    def is_safe(row, col):
        for r, c in enumerate(queens):
            if c == col:                    # same column
                return False
            if abs(r - row) == abs(c - col):  # same diagonal
                return False
        return True

    def backtrack(row):
        if row == n:
            board = []
            for c in queens:
                board.append("." * c + "Q" + "." * (n - c - 1))
            solutions.append(board)
            return
        for col in range(n):
            if is_safe(row, col):
                queens.append(col)
                backtrack(row + 1)
                queens.pop()

    backtrack(0)
    return solutions


for n in [4, 5]:
    solutions = solve_n_queens(n)
    print(f"\n{n}-Queens: {len(solutions)} solution(s)")
    if solutions:
        print(f"First solution:")
        for row in solutions[0]:
            print(f"  {row}")

# ---------------------------------------------------------
# 4. Sudoku Solver
# ---------------------------------------------------------
print("\n=== Sudoku Solver ===")

def solve_sudoku(board):
    """
    Solve a 9×9 Sudoku puzzle in-place using backtracking.

    Args:
        board (list[list[int]]): 9×9 grid, 0 = empty cell.

    Returns:
        bool: True if solved, False if no solution exists.
    """
    def is_valid(board, row, col, num):
        # Check row
        if num in board[row]:
            return False
        # Check column
        if num in (board[r][col] for r in range(9)):
            return False
        # Check 3×3 box
        box_r, box_c = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_r, box_r + 3):
            for c in range(box_c, box_c + 3):
                if board[r][c] == num:
                    return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for num in range(1, 10):
                        if is_valid(board, r, c, num):
                            board[r][c] = num
                            if backtrack():
                                return True
                            board[r][c] = 0     # undo
                    return False    # no valid number, backtrack
        return True     # board fully filled

    return backtrack()


def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("  " + "-" * 21)
        row_str = ""
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += (str(val) if val != 0 else ".") + " "
        print(f"  {row_str}")


puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

print("Puzzle:")
print_board(puzzle)

solved = solve_sudoku(puzzle)
if solved:
    print("\nSolution:")
    print_board(puzzle)

# ---------------------------------------------------------
# 5. Combination Sum
# ---------------------------------------------------------
print("\n=== Combination Sum ===")

def combination_sum(candidates, target):
    """
    Find all unique combinations of candidates that sum to target.
    Each candidate can be used multiple times.

    Time:  O(n^(target/min)) in worst case
    """
    candidates.sort()
    result = []

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()

    backtrack(0, [], target)
    return result


combos = combination_sum([2, 3, 6, 7], 7)
print(f"combination_sum([2,3,6,7], 7):")
for c in combos:
    print(f"  {c} (sum={sum(c)})")
