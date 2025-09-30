"""
Given an integer n. You need to generate all the binary strings of n characters representing bits.

Note: Return the strings in  ascending order.
"""

class Solution:
    def binstr(self, n):
        result = []
        for i in range(2 ** n):
            result.append(format(i, '0{}b'.format(n)))
        return result
