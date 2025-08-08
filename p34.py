"""
Given a string s, of lowercase english alphabets, find the length of the longest proper prefix which is also a suffix.
Note: Prefix and suffix can be overlapping but they should not be equal to the entire string.
"""
class Solution:
    def getLPSLength(self, s):
        n = len(s)
        lps = [0] * n  # lps[i] = length of longest prefix-suffix for s[:i+1]
        length = 0  # length of previous longest prefix-suffix

        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps[-1] if n > 0 else 0
