"""
You are given a 0-indexed integer array nums consisting of 3 * n elements.
You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:
The first n elements belonging to the first part and their sum is sumfirst.
The next n elements belonging to the second part and their sum is sumsecond.
The difference in sums of the two parts is denoted as sumfirst - sumsecond.
For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.
"""

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 3
        total = len(nums)

    # Step 1: Left part - for each i, what's the smallest sum we can get by picking n numbers from first i
        left = [0] * (2*n+1)
        max_heap = []
        left_sum = 0
    
    # First, pick n numbers, and fill the heap
        for i in range(n):
            left_sum += nums[i]
            heapq.heappush(max_heap, -nums[i])   # max-heap using negative numbers
    
        left[n] = left_sum
    # Now, for each next number add to heap, possibly replace max in heap (to keep smallest sum)
        for i in range(n, 2*n):
            heapq.heappush(max_heap, -nums[i])
            left_sum += nums[i]
            left_sum += heapq.heappop(max_heap)  # Remove largest (smallest negative) -- keep n smallest
            left[i+1] = left_sum

    # Step 2: Right part - for each i, what's the largest sum we can get by picking n from last i
        right = [0] * (2*n+1)
        min_heap = []
        right_sum = 0
    
    # First, pick n numbers from the end, and fill min-heap
        for i in range(total-1, total-n-1, -1):
            right_sum += nums[i]
            heapq.heappush(min_heap, nums[i])  # min-heap
    
        right[2*n] = right_sum
    # Now, for previous numbers, possibly replace min to keep largest sum
        for i in range(2*n-1, n-1, -1):
            heapq.heappush(min_heap, nums[i])
            right_sum += nums[i]
            right_sum -= heapq.heappop(min_heap)  # Remove smallest (keep n largest)
            right[i] = right_sum
    
    # Step 3: The answer is the minimum left - right for each split
        answer = float('inf')
        for i in range(n, 2*n+1):
            answer = min(answer, left[i] - right[i])
        return answer
        
