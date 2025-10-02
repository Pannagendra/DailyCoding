"""
Given two integers n and k, the task is to find all valid combinations of k numbers that adds up to n based on the following conditions:

    Only numbers from the range [1, 9] used.
    Each number can only be used at most once.

Note: You can return the combinations in any order, the driver code will print them in sorted order.
"""
class Solution:
    def combinationSum(self, n, k):
        result = []
        
        def backtrack(start, path, total):
            if len(path) == k:
                if total == n:
                    result.append(path[:])
                return
            for num in range(start, 10):
                if total + num > n:
                    break
                path.append(num)
                backtrack(num + 1, path, total + num)
                path.pop()
                
        backtrack(1, [], 0)
        return result
