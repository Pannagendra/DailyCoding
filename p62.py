"""
You have a row of flowers, where each flower blooms after a specific day. 
The array arr[] represents the blooming schedule: arr[i] is the day the flower at position i will bloom. 
To create a bouquet, you need to collect k adjacent bloomed flowers. Each flower can only be used in one bouquet.

Your goal is to find the minimum number of days required to make exactly m bouquets. If it is not possible to make m bouquets with the given arrangement, return -1.
"""
class Solution:
    def minDaysBloom(self, arr, k, m):
        n = len(arr)
        
        # Not enough flowers to make m bouquets
        if n < k * m:
            return -1
        
        def canMake(day):
            bouquets = 0
            flowers = 0
            for bloom in arr:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m:
                    return True
            return False
        
        low, high = min(arr), max(arr)
        while low < high:
            mid = (low + high) // 2
            if canMake(mid):
                high = mid
            else:
                low = mid + 1
        
        return low if canMake(low) else -1
