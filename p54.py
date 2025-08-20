"""
You are given a 2D matrix mat[][] of size n x m that was initially filled in the following manner:

    Each row is sorted in increasing order from left to right.
    The first element of every row is greater than the last element of the previous row.

This implies that if the matrix is flattened row-wise, it forms a strictly sorted 1D array.
Later, this sorted 1D array was rotated at some unknown pivot. The rotated array was then written back into the matrix row-wise to form the current matrix.

Given such a matrix mat[][] and an integer x, determine whether x exists in the matrix.
"""
class Solution:
    def searchMatrix(self, mat, x):
        if not mat or not mat[0]:
            return False
        
        n, m = len(mat), len(mat[0])
        left, right = 0, n * m - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Convert 1D index to 2D coordinates
            mid_val = mat[mid // m][mid % m]
            
            if mid_val == x:
                return True
            
            # Determine which half is sorted
            left_val = mat[left // m][left % m]
            right_val = mat[right // m][right % m]
            
            if left_val <= mid_val:
                # Left half is sorted
                if left_val <= x < mid_val:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted  
                if mid_val < x <= right_val:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
