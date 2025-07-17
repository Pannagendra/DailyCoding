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

            # Check if the complement already exists in the dictionary.
            # If it does, the two numbers have been found.
            if complement in num_map:
                # Return the index of the complement and the current number's index.
                print("yes complement in num_map at index ",  [num_map[complement], i] )
                return [num_map[complement], i]

            # If the complement is not found, add the current number and its index to the dictionary.
            num_map[num] = i
            print("No complement is not in num_map", num_map[num] )

        # If no solution is found (though the problem statement guarantees one exists),
        # an empty list can be returned or an error could be raised.
        # For this problem, exactly one solution is guaranteed.
        return []
