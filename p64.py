"""
Given an array arr[] consisting of positive integers and an integer k. You are allowed to perform at most k operations, where in each operation, you can increment any one element of the array by 1. Determine the maximum possible median of the array that can be achieved after performing at most k such operations.

Note: The median of a sorted array is the middle element if the size is odd, or the average of the two middle elements if the size is even.
"""
class Solution:
    def maximizeMedian(self, arr, k):
        arr.sort()
        n = len(arr)

        def isPossible(target):
            used = 0
            if n % 2 == 1:
                # For odd length: raise elements from median index onward
                mid = n // 2
                for i in range(mid, n):
                    if arr[i] < target:
                        used += target - arr[i]
            else:
                # For even length: both middle elements plus elements to the right
                left_mid = n // 2 - 1
                right_mid = n // 2
                if arr[right_mid] <= target:
                    used += max(0, target - arr[right_mid])
                    used += max(0, target - arr[left_mid])
                else:
                    used += max(0, 2 * target - (arr[right_mid] + arr[left_mid]))
                for i in range(right_mid + 1, n):
                    if arr[i] < target:
                        used += target - arr[i]
            return used <= k

        # Compute initial median as floor of average of middle two (if even)
        if n % 2 == 1:
            iniMedian = arr[n // 2]
        else:
            iniMedian = (arr[n // 2] + arr[n // 2 - 1]) // 2

        left, right = iniMedian, iniMedian + k
        answer = iniMedian

        while left <= right:
            mid = (left + right) // 2
            if isPossible(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
