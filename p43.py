"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

    It is a substring of num with length 3.
    It consists of only one unique digit.

Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

    A substring is a contiguous sequence of characters within a string.
    There may be leading zeroes in num or a good integer.
"""

class Solution(object):
  def maxgoodInteger(self, num):
    max_good=""
    for i in range(len(num)-2):
      substring = num[i:i+2]
      if substring[0]==substring[1] == substring[2]:
        if substring > max_good:
          max_good = substring
    return max_good
