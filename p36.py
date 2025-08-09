"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # A power of two has only one bit set in its binary representation.
        # n > 0 ensures we're dealing with positive integers.
        return n > 0 and (n & (n - 1)) == 0
