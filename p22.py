"""
Given an array arr[] and an integer k, the task is to find the length of longest subarray in which the count of elements greater than k is more than the count of elements less than or equal to k.
"""


class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        # val will hold +1 (for >k) and -1 (for <=k)
        val = [1 if x > k else -1 for x in arr]

        prefix_sum = 0
        # Store: first occurrence of a particular prefix sum
        first_occurrence = {0: -1}
        max_len = 0

        for i, v in enumerate(val):
            prefix_sum += v

            # If prefix_sum > 0 at this point, whole subarray [0...i] is valid
            if prefix_sum > 0:
                max_len = i + 1
            else:
                # We want prefix_sum - 1 to have occurred before, meaning the sum from that point to here is > 0
                want = prefix_sum - 1
                if want in first_occurrence:
                    max_len = max(max_len, i - first_occurrence[want])

            # Store earliest occurrence
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i

        return max_len
