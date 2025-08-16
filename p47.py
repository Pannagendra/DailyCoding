"""
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""
class Solution(object):
  def max69number(self, num):
    num_str = str(num)
    max_str = num_str.replace('6','9',1)
    return int(max_str)
