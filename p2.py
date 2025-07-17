#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store numbers and their indices.
        # The keys will be the numbers, and the values will be their indices.
        num_map = {}
        print("Empty dictionary", num_map)
        # Iterate through the array with both index and value using enumerate.
        for i, num in enumerate(nums):
            # Calculate the complement (the number needed to reach the target).
            complement = target - num
            
            print("target", target)
            print("num", num)
            print("complement", complement)
