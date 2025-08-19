"""
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

class Solution(object):
  def nonemptyzeroarray(self,nums):
    count=0
    result=0
    for num in nums:
      if num == 0:
        count+=1
        result+=count
      else:
        count=0
    return result
