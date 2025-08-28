"""
You are given an n x n square matrix of integers grid. Return the matrix such that:

    The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
    The diagonals in the top-right triangle are sorted in non-decreasing order.

"""
class Solution:
    def sortMatrix(self, grid):
        n = len(grid)

        for i in range(n):
            tmp = [grid[i + j][j] for j in range(n - i)]
            tmp.sort(reverse=True)
            for j in range(n - i):
                grid[i + j][j] = tmp[j]

        for j in range(1, n):
            tmp = [grid[i][j + i] for i in range(n - j)]
            tmp.sort()
            for i in range(n - j):
                grid[i][j + i] = tmp[i]

        return grid
