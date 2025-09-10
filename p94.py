"""
Given a string s, return the lexicographically largest string that can be obtained by swapping at most one pair of characters in s.
"""
class Solution:
    def largestSwap(self, s):
        arr = list(s)  # Strings are immutable; convert to a list
        n = len(arr)
        max_char = ''
        max_index = -1
        l, r = -1, -1

        # Traverse from right to left to find the largest char for a possible swap
        for i in range(n - 1, -1, -1):
            if arr[i] > max_char:
                max_char = arr[i]
                max_index = i
            elif arr[i] < max_char:
                l, r = i, max_index

        # If a valid pair is found, perform the swap
        if l != -1:
            arr[l], arr[r] = arr[r], arr[l]
        
        return ''.join(arr)
