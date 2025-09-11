"""
You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

For example:

    If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
    If arr[i] = 0, you cannot jump forward from that position.

Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

Note:  Return -1 if you can't reach the end of the array.


Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
Output: 3 
Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. 
"""
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # Edge case: if array has 1 element, we are already at the end
        if n <= 1:
            return 0
        
        # If the first element is 0, we can't move anywhere
        if arr[0] == 0:
            return -1
        
        # Initialize variables
        maxReach = arr[0]   # farthest index we can reach
        steps = arr[0]      # steps we can still take
        jumps = 1           # we take at least one jump
        
        for i in range(1, n):
            # If we reach the end
            if i == n - 1:
                return jumps
            
            # Update maxReach
            maxReach = max(maxReach, i + arr[i])
            
            # Use a step
            steps -= 1
            
            # If no steps left, we must make another jump
            if steps == 0:
                jumps += 1
                # If current index is >= maxReach, we cannot move forward
                if i >= maxReach:
                    return -1
                # Reinitialize steps for the new jump
                steps = maxReach - i
        
        return -1
