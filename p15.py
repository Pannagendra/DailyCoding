"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Always binary-search the **smaller** array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2          # #-of elements in the combined left half

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2                 # cut in nums1
            j = total_left - i                 # cut in nums2 (coupled)

            left1  = nums1[i - 1] if i else float('-inf')
            right1 = nums1[i]     if i < m else float('inf')
            left2  = nums2[j - 1] if j else float('-inf')
            right2 = nums2[j]     if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:      # correct partition
                if (m + n) % 2:                          # odd length
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:                         # too far right in nums1
                hi = i - 1
            else:                                        # too far left in nums1
                lo = i + 1
