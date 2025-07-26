"""
You are given an integer n which represents an array nums containing the numbers from 1 to n in order. Additionally, you are given a 2D array conflictingPairs, where conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair.

Remove exactly one element from conflictingPairs. Afterward, count the number of

of nums which do not contain both a and b for any remaining conflicting pair [a, b].

Return the maximum number of subarrays possible after removing exactly one conflicting pair.
"""

class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        """
        :type n: int
        :type conflictingPairs: List[List[int]]
        :rtype: int
        """
        validSubarrays = 0
        maxLeft = 0
        secondMaxLeft = 0
        
        # gains[i] := additional valid subarrays we gain if restriction at index i is removed
        gains = [0] * (n + 1)
        
        # conflicts[r] := left endpoints that conflict with subarrays ending at r
        conflicts = [[] for _ in range(n + 1)]
        
        # Group conflicts by their right endpoint
        for a, b in conflictingPairs:
            conflicts[max(a, b)].append(min(a, b))
        
        # Process each position from left to right
        for right in range(1, n + 1):
            # Update the most restrictive conflicts for subarrays ending at 'right'
            for left in conflicts[right]:
                if left > maxLeft:
                    secondMaxLeft = maxLeft
                    maxLeft = left
                elif left > secondMaxLeft:
                    secondMaxLeft = left
            
            # Count valid subarrays ending at 'right'
            # These are [maxLeft + 1, right], [maxLeft + 2, right], ..., [right, right]
            validSubarrays += right - maxLeft
            
            # Calculate potential gain if we remove the most restrictive conflict
            # If we remove maxLeft, we gain subarrays from [secondMaxLeft + 1, right] to [maxLeft, right]
            gains[maxLeft] += maxLeft - secondMaxLeft
        
        return validSubarrays + max(gains)
