#You are given an integer array nums.

#A subsequence sub of nums with length x is called valid if it satisfies:
#(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
#Return the length of the longest valid subsequence of nums.
#A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        
        # dp[i][parity] = maximum length of valid subsequence ending at index i 
        # with the last pair having the given parity
        dp = {}
        max_len = 2  # At least 2 elements needed for a valid subsequence
        
        # Initialize: every pair of elements can form a subsequence of length 2
        for i in range(n):
            for j in range(i + 1, n):
                parity = (nums[i] + nums[j]) % 2
                dp[(j, parity)] = 2
        
        # Fill DP table
        for i in range(n):
            for j in range(i + 1, n):
                parity = (nums[i] + nums[j]) % 2
                
                # Try to extend existing subsequences ending at index i
                if (i, parity) in dp:
                    dp[(j, parity)] = max(dp.get((j, parity), 2), dp[(i, parity)] + 1)
                
                max_len = max(max_len, dp[(j, parity)])
        
        return max_len
