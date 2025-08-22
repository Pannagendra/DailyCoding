"""
You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.
"""
class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid),len(grid[0])
        min_rows, max_row = rows,-1
        min_col,max_col = cols,-1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    min_rows = min(min_rows,r)
                    max_row = max(max_row,r)
                    min_col = min(min_col,c)
                    max_col = max(max_col,c)
        if max_row ==-1:
            return 0
        return (max_row - min_rows + 1) * (max_col - min_col + 1)
