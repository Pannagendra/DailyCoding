"""
You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.

Return the minimum possible sum of the area of these rectangles.

Note that the rectangles are allowed to touch.
"""
class Solution(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        ones = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]
        if not ones:
            return 0

        INF = float("inf")
        
        def rect_area(points):
            """Bounding box area covering given points"""
            if not points:
                return 0
            r1 = min(p[0] for p in points)
            r2 = max(p[0] for p in points)
            c1 = min(p[1] for p in points)
            c2 = max(p[1] for p in points)
            return (r2 - r1 + 1) * (c2 - c1 + 1)

        ans = INF

        # --- Case 1: Vertical partition ---
        for c1 in range(m - 2):
            for c2 in range(c1 + 1, m - 1):
                g1 = [(i, j) for (i, j) in ones if j <= c1]
                g2 = [(i, j) for (i, j) in ones if c1 < j <= c2]
                g3 = [(i, j) for (i, j) in ones if j > c2]
                if g1 and g2 and g3:
                    ans = min(ans, rect_area(g1) + rect_area(g2) + rect_area(g3))

        # --- Case 2: Horizontal partition ---
        for r1 in range(n - 2):
            for r2 in range(r1 + 1, n - 1):
                g1 = [(i, j) for (i, j) in ones if i <= r1]
                g2 = [(i, j) for (i, j) in ones if r1 < i <= r2]
                g3 = [(i, j) for (i, j) in ones if i > r2]
                if g1 and g2 and g3:
                    ans = min(ans, rect_area(g1) + rect_area(g2) + rect_area(g3))

        # --- Case 3: Mixed partitions (vertical + horizontal) ---
                # --- Case 3: Mixed partitions (row + col cut) ---
        for cut_row in range(n - 1):
            for cut_col in range(m - 1):
                TL = [(i, j) for (i, j) in ones if i <= cut_row and j <= cut_col]
                TR = [(i, j) for (i, j) in ones if i <= cut_row and j > cut_col]
                BL = [(i, j) for (i, j) in ones if i > cut_row and j <= cut_col]
                BR = [(i, j) for (i, j) in ones if i > cut_row and j > cut_col]

                # Merge TL+TR (top), keep BL, BR
                if (TL or TR) and BL and BR:
                    ans = min(ans, rect_area(TL+TR) + rect_area(BL) + rect_area(BR))

                # Merge BL+BR (bottom), keep TL, TR
                if (BL or BR) and TL and TR:
                    ans = min(ans, rect_area(BL+BR) + rect_area(TL) + rect_area(TR))

                # Merge TL+BL (left), keep TR, BR
                if (TL or BL) and TR and BR:
                    ans = min(ans, rect_area(TL+BL) + rect_area(TR) + rect_area(BR))

                # Merge TR+BR (right), keep TL, BL
                if (TR or BR) and TL and BL:
                    ans = min(ans, rect_area(TR+BR) + rect_area(TL) + rect_area(BL))

        return ans if ans < INF else 0
