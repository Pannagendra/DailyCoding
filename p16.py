"""
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

    In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.

Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.
"""
class Solution(obejct):
  def longestSubarray(self,nums):
    max_num = len (nums)
    max_len = 0
    cur_len =0
    for num in nums:
      if num == max_num:
        cur_len +=1
        max_len= max(max_len, cur_len)
      else:
        cur_len = 0
    return max_len
