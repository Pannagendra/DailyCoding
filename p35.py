"""
Given a string s, find the length of longest periodic proper prefix of s. If no such prefix exists, return -1.
A periodic proper prefix is a non empty prefix of s (but not the whole string), such that repeating this prefix enough times produces a string that starts with s.
"""
class Solution:
    def getLongestPrefix(self, s):
        n = len(s)
        if n <= 1:
            return -1

        # Compute Z-function
        Z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r:
                Z[i] = min(r - i + 1, Z[i - l])
            while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                Z[i] += 1
            if i + Z[i] - 1 > r:
                l, r = i, i + Z[i] - 1

        # Check from longest to shortest proper prefix
        for L in range(n - 1, 0, -1):
            if Z[L] >= n - L:  # Prefix of length L covers the rest
                return L
        return -1
