"""
You are given an array arr[]. For each element at index i (0-based indexing), find the farthest index j to the right (i.e., j > i) such that arr[j] < arr[i]. 
If no such index exists for a given position, return -1 for that index. Return the resulting array of answers.
"""
class Solution(object):
  def slefmin(self, arr):
    n = len(arr)
    result = [-1] * n
    suff_min = [0] * n
    suff_min[-1] = arr [-1]
    for i in range(n-2,-1,-1):
      suff_min[i] = min(arr[i], suff_min[i+1])

            # Step 2: For each i, binary search the farthest j
    for i in range(n - 1):  # 👈 skip last index
        if suff_min[i + 1] >= arr[i]:  # no smaller element exists
            continue
            
        lo, hi = i + 1, n - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if suff_min[mid] < arr[i]:
                ans = mid
                lo = mid + 1   # search farther
            else:
                hi = mid - 1
        result[i] = ans
        
    return result
