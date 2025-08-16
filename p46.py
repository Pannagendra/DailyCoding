"""
Given an array of integers arr[] representing non-negative integers, arrange them so that after concatenating all of them in order, 
it results in the largest possible number. Since the result may be very large, return it as a string.
"""
class Solution(object):
  def concatnumbers(self, arr):
    arr = list(map(str,arr))
    arr.sort(key=lambda x:x*10, reverse=True)
    result=''.join(arr)
    return result.lstrip('0') or 0
    
