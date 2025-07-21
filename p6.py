"""
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique."""

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
      result = []
      for c in s:
        if len(result)>=2 and result[-1] == result[-2] == c:
          continue
        result.append(c)
      return ''.join(result)
