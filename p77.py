"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

We need to fill a 9x9 Sudoku board so that:

Each row has digits 1–9 exactly once.

Each column has digits 1–9 exactly once.

Each 3x3 subgrid (box) has digits 1–9 exactly once.

Empty cells are marked as ".".

Algorithm Used: Backtracking with Constraint Tracking

The idea is:

Try filling empty cells one by one.

At each empty cell, try digits 1–9.

If the placement violates Sudoku rules → skip.

If valid → place it and continue with recursion.

If no digit works → backtrack (undo previous placements).
"""

class Solution:
    def solveSudoku(self, board):
        """
        Optimized Sudoku solver using backtracking + constraint tracking.
        :param board: List[List[str]]
        """

        # Track used numbers in rows, cols, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []  # store empty cells

        # Initialize trackers
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(i=0):
            if i == len(empties):
                return True  # all filled

            r, c = empties[i]
            b = (r // 3) * 3 + (c // 3)

            for ch in map(str, range(1, 10)):
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[b]:
                    # place number
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[b].add(ch)

                    if backtrack(i + 1):
                        return True

                    # undo placement
                    board[r][c] = '.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[b].remove(ch)

            return False

        backtrack()
