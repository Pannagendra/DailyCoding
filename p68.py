"""
You are given a 2D 0-indexed integer array dimensions.

For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.

Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.
"""
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_diag = -1
        max_area = -1
        
        for l, w in dimensions:
            diag_sq = l * l + w * w
            area = l * w
            
            if diag_sq > max_diag:
                max_diag = diag_sq
                max_area = area
            elif diag_sq == max_diag:
                if area > max_area:
                    max_area = area
        return max_area
