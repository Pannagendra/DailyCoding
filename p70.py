"""
Given an integer array arr[]. Find the number of triangles that can be formed with three different array elements as lengths of three sides of the triangle.
A triangle with three given sides is only possible if sum of any two sides is always greater than the third side.
"""
class Solution:
    def countTriangles(self, arr):
        n = len(arr)
        arr.sort()
        count = 0

        # Fix the third side one by one
        for k in range(n-1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    # All elements between i and j form a triangle with arr[j] and arr[k]
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count
