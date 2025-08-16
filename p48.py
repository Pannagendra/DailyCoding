"""
Given an m x n matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.
"""
class Solution(object):
  def smallestcommonelement(self,mat):
    m = len(mat)
    from collections import Counter
    counter = Counter()
    for row in mat:
      counter.update(row)
    for num in sorted(counter):
      if counter[num]==m:
        return num
    return -1
