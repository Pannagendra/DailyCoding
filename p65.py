"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
"""
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        
        for d in range(m + n - 1):
            intermediate = []
            
            # Start row for this diagonal
            r = 0 if d < n else d - n + 1
            # Start col for this diagonal
            c = d if d < n else n - 1
            
            # Collect diagonal elements
            while r < m and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            
            # Reverse order on even diagonals
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        
        return result
