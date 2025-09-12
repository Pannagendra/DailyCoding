"""
Given an array arr[] denoting heights of n towers and a positive integer k.

For each tower, you must perform exactly one of the following operations exactly once.

    Increase the height of the tower by k
    Decrease the height of the tower by k

Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by k for each tower. After the operation, the resultant array should not contain any negative integers.
"""

class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        # Initial difference without modifications
        ans = arr[-1] - arr[0]
        
        # The smallest and largest after applying +k/-k
        smallest = arr[0] + k
        largest = arr[-1] - k
        
        for i in range(n - 1):
            min_h = min(smallest, arr[i+1] - k)
            max_h = max(largest, arr[i] + k)
            
            if min_h < 0:  # skip invalid (negative height)
                continue
            
            ans = min(ans, max_h - min_h)
        
        return ans
