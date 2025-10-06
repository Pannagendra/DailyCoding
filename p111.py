"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
"""
class Solution(object):
    def swimInWater(self, grid):
        N = len(grid)

        seen = {(0, 0)}
        pq = [(grid[0][0], 0, 0)]
        ans = 0
        while pq:
            d, r, c = heapq.heappop(pq)
            ans = max(ans, d)
            if r == c == N-1: return ans
            for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen:
                    heapq.heappush(pq, (grid[cr][cc], cr, cc))
                    seen.add((cr, cc))
