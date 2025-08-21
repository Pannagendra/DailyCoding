"""
Given an array arr[] of integers and an integer k, 
select k elements from the array such that the minimum absolute difference between any 
two of the selected elements is maximized. Return this maximum possible minimum difference.
"""
class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        
        def isPossible(mid):
            cnt = 1           # first element is always picked
            last = arr[0]
            for i in range(1, len(arr)):
                if arr[i] - last >= mid:
                    cnt += 1
                    last = arr[i]
                    if cnt == k:
                        return True
            return False
        
        low = 0
        high = arr[-1] - arr[0]
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            if isPossible(mid):
                answer = mid
                low = mid + 1 # try for larger minimum difference
            else:
                high = mid - 1
        return answer
