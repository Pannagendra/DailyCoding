"""
Given a 2D matrix mat[][] with dimensions n×m. Find the maximum possible sum of any submatrix within the given matrix.
"""
class Solution:
    def maxRectSum(self, mat):
        if not mat or not mat[0]:
            return 0
        
        n = len(mat)
        m = len(mat[0])
        max_sum = float('-inf')
        
        # Loop over all pairs of rows
        for top in range(n):
            temp = [0] * m
            for bottom in range(top, n):
                # Add current row to temp, to create the "column sum" between rows top and bottom
                for col in range(m):
                    temp[col] += mat[bottom][col]
                
                # Now apply 1D Kadane's algorithm on temp
                curr_sum = 0
                max_ending_here = float('-inf')
                for val in temp:
                    curr_sum = max(val, curr_sum + val)
                    max_ending_here = max(max_ending_here, curr_sum)
                
                max_sum = max(max_sum, max_ending_here)
        
        return max_sum
