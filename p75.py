"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

The algorithm to validate a Sudoku board works by ensuring three key constraints are met for every filled cell:

    Each digit 1-9 can appear only once in each row.

    Each digit 1-9 can appear only once in each column.

    Each digit 1-9 can appear only once in each of the nine 3x3 sub-boxes.

Approach Explanation:

    Data Structures Used: Three arrays of sets are created to keep track of digits seen so far in every row, every column, and every 3x3 sub-box (also called sub-matrix or sub-grid).

    Iteration: The algorithm iterates over every cell of the 9x9 board.

    Skip Empty Cells: If the cell is empty (denoted by '.' or '0'), it is skipped since only filled cells need validation.

    Check Constraints:

        For the row of the current cell, check if the digit is already present in the corresponding row's set. If yes, it violates Sudoku rules and returns False.

        For the column of the current cell, check the corresponding column's set similarly.

        For the 3x3 sub-box, an index is computed using box_index=(r//3)×3+(c//3)box_index=(r//3)×3+(c//3), where r,cr,c are row and column indices. Check the corresponding sub-box's set for duplicates.

    Add the digit to respective sets: If no duplicates in row, column, or box, add this digit to these sets to track usage.

    Final Result: If after scanning all cells no duplicates are found, return True meaning the board complies with Sudoku rules (although it might not necessarily be solvable).

Efficiency:

    Time Complexity: O(92)=O(81)O(92)=O(81), fixed for standard Sudoku.

    Space Complexity: O(9×9)O(9×9) due to the sets used for rows, columns, and boxes.

This straightforward method efficiently validates that the partial Sudoku board is currently valid with respect to the unique appearance of digits in rows, columns, and boxes.
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Use sets to track seen numbers for rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue  # Empty cell, skip
                # Check row
                if val in rows[r]:
                    return False
                rows[r].add(val)
                # Check column
                if val in cols[c]:
                    return False
                cols[c].add(val)
                # Check sub-box
                box_idx = (r // 3) * 3 + (c // 3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)
        return True
