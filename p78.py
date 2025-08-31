"""
Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the vertical lines, find the maximum amount of water that can be contained between any two lines, together with the x-axis.

Note: In the case of a single vertical line it will not be able to hold water.

🔎 Problem Understanding

Each index i represents a vertical line of height arr[i].

The amount of water between two lines i and j is:

Water=min⁡(arr[i],arr[j])×(j−i)
Water=min(arr[i],arr[j])×(j−i)

(because the height is limited by the shorter line, and the width is j - i).

⚡ Algorithm: Two-Pointer Approach

Place one pointer at the start (left = 0) and one at the end (right = n-1).

Compute the area formed by arr[left] and arr[right].

Move the pointer pointing to the shorter line, because moving the taller one can’t improve the area (height is limited by the shorter line).

Repeat until pointers meet.

Keep track of the maximum area.

⏱ Time Complexity: O(n)
📦 Space Complexity: O(1)
"""

class Solution:
    def maxWater(self, arr):
        left, right = 0, len(arr) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            height = min(arr[left], arr[right])
            width = right - left
            max_area = max(max_area, height * width)
            
            # Move the pointer of the shorter line
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
