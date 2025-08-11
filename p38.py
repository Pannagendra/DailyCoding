"""
Given a string s consisting of lowercase English letters, find the maximum possible sum of the lengths of any two non-empty and non-overlapping palindromic substrings of odd length.

Formally, choose any two substrings s[i...j] and s[k...l] such that 1 ≤ i ≤ j < k ≤ l ≤ s.size(), both substrings are palindromes of odd length, and they do not overlap. Return the maximum sum of their lengths.

Note: A palindrome is a string that reads the same forward and backward. A substring is a contiguous sequence of characters within the string.
"""
class Solution:
    def maxSum(self, s):
        n = len(s)
        if n < 2:
            return 0
        
        # For identical characters, use mathematical formula
        # If all characters are same, any substring is a palindrome
        # For length n, max palindrome lengths at each split are:
        # left part of length i can have max palindrome of length i (if i is odd) or i-1 (if i is even)
        # right part of length n-i can have max palindrome of length n-i (if n-i is odd) or n-i-1 (if n-i is even)
        
        # Check if string has all identical characters
        all_same = True
        for i in range(1, n):
            if s[i] != s[0]:
                all_same = False
                break
        
        if all_same:
            # For string of identical chars, find optimal split
            max_sum = 0
            for i in range(1, n):  # split after position i-1
                # Left part: s[0...i-1] has length i
                # Right part: s[i...n-1] has length n-i
                left_len = i
                right_len = n - i
                
                # Maximum odd palindrome length for each part
                left_max = left_len if left_len % 2 == 1 else left_len - 1
                right_max = right_len if right_len % 2 == 1 else right_len - 1
                
                max_sum = max(max_sum, left_max + right_max)
            
            return max_sum
        
        # For mixed characters, use optimized approach with early termination
        # Use Manacher's algorithm concept but simplified
        def get_max_odd_palindrome_lengths():
            # Get maximum odd palindrome ending at each position
            left_max = [1] * n  # minimum is single character
            # Get maximum odd palindrome starting at each position  
            right_max = [1] * n
            
            # For each center, expand and update relevant positions
            for center in range(n):
                radius = 0
                # Expand around center
                while (center - radius >= 0 and 
                       center + radius < n and 
                       s[center - radius] == s[center + radius]):
                    
                    # Update left_max for ending positions
                    end_pos = center + radius
                    left_max[end_pos] = max(left_max[end_pos], 2 * radius + 1)
                    
                    # Update right_max for starting positions  
                    start_pos = center - radius
                    right_max[start_pos] = max(right_max[start_pos], 2 * radius + 1)
                    
                    radius += 1
            
            # Forward pass for left_max - carry forward maximum seen so far
            for i in range(1, n):
                left_max[i] = max(left_max[i], left_max[i-1])
            
            # Backward pass for right_max - carry backward maximum seen so far
            for i in range(n-2, -1, -1):
                right_max[i] = max(right_max[i], right_max[i+1])
                
            return left_max, right_max
        
        left_max, right_max = get_max_odd_palindrome_lengths()
        
        # Find maximum sum across all split points
        max_sum = 0
        for i in range(n - 1):
            # Split after position i: left part [0...i], right part [i+1...n-1]
            max_sum = max(max_sum, left_max[i] + right_max[i + 1])
        
        return max_sum
