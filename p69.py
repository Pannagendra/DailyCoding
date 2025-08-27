"""
You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.

A V-shaped diagonal segment is defined as:

    The segment starts with 1.
    The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
    The segment:
        Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
        Continues the sequence in the same diagonal direction.
        Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.


"""
class Solution:
    def lenOfVDiagonal(self, grid):
        DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(cx, cy, direction, turn, target):
            nx, ny = cx + DIRS[direction][0], cy + DIRS[direction][1]
            # If it goes beyond the boundary or the next node's value is not the target value, then return
            if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != target:
                return 0
            turn_int = 1 if turn else 0
            # Continue walking in the original direction.
            max_step = dfs(nx, ny, direction, turn, 2 - target)
            if turn:
                # Clockwise rotate 90 degrees turn
                max_step = max(
                    max_step,
                    dfs(nx, ny, (direction + 1) % 4, False, 2 - target),
                )
            return max_step + 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for direction in range(4):
                        res = max(res, dfs(i, j, direction, True, 2) + 1)
        return res
