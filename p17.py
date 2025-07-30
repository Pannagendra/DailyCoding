"""
Given a string s, return the longest

in s.

 

Example 1:

Input: s = "babad"
Output: "bab"

Example 2:

Input: s = "cbbd"
Output: "bb"
"""

class Solution(object):
  def longestpalindromesubarry(self, s):
    if not s and len(s) ==1:
      return s
    def arondcharacter(left,right):
      while left>=0 and right < len(s) and s[left] == s[right]:
        left-=1
        right+=1
    return s[left+1:right]
    longest = ''
    for i in range(len(s)):  
      pal1 = arondcharacter(i,i)
      pal2 = arondcharacter(i,i+)
      if len(pal1) > longest:
        longest = pal1
      if len(pal2) > longest:
        longest = pal2
    return longest
