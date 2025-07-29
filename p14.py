"""
You are given a 0-indexed array nums of length n, consisting of non-negative integers. For each index i from 0 to n - 1, you must determine the size of the minimum sized non-empty subarray of nums starting at i 
(inclusive) that has the maximum possible bitwise OR.

    In other words, let Bij be the bitwise OR of the subarray nums[i...j]. 
    You need to find the smallest subarray starting at i, such that bitwise OR of this subarray is equal to max(Bik) 
    where i <= k <= n - 1.

The bitwise OR of an array is the bitwise OR of all the numbers in it.

Return an integer array answer of size n where answer[i] is the length of the minimum sized subarray starting at i with maximum bitwise OR.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
class solution(self):
  def smallestSubarrays(self,nums):
    n = len(nums)
    answer = [0] * n
    rightmost=[-1] * 30
    for i in range(n-1,-1,-1):
      for bit in range(30):
        if (nums[i] & (1 << bit)):
          rightmost[bit] =i
      max_reach = i
      for bit in range(30):
        if rightmost[bit] != -1:
        max_reach = max(max_reach, rightmost[bit])
      answer[i] = max_reach - i + 1
    return answer
