"""
You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

    Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
    Each basket can hold only one type of fruit.
    If a fruit type cannot be placed in any basket, it remains unplaced.

Return the number of fruit types that remain unplaced after all possible allocations are made.
"""
class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(baskets)
        
        # Create a segment tree to efficiently find leftmost available basket
        # Tree stores the maximum capacity in each range
        tree = [0] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                tree[node] = baskets[start]
            else:
                mid = (start + end) // 2
                build(2 * node, start, mid)
                build(2 * node + 1, mid + 1, end)
                tree[node] = max(tree[2 * node], tree[2 * node + 1])
        
        def query_and_update(node, start, end, fruit_size):
            # Find leftmost basket that can fit fruit_size and mark it as used
            if start == end:
                if tree[node] >= fruit_size:
                    tree[node] = 0  # Mark as used
                    return start
                return -1
            
            mid = (start + end) // 2
            # Try left subtree first (leftmost)
            if tree[2 * node] >= fruit_size:
                result = query_and_update(2 * node, start, mid, fruit_size)
                if result != -1:
                    tree[node] = max(tree[2 * node], tree[2 * node + 1])
                    return result
            
            # Try right subtree if left failed
            if tree[2 * node + 1] >= fruit_size:
                result = query_and_update(2 * node + 1, mid + 1, end, fruit_size)
                if result != -1:
                    tree[node] = max(tree[2 * node], tree[2 * node + 1])
                    return result
            
            return -1
        
        if n == 0:
            return len(fruits)
        
        build(1, 0, n - 1)
        
        unplaced = 0
        for fruit in fruits:
            result = query_and_update(1, 0, n - 1, fruit)
            if result == -1:
                unplaced += 1
        
        return unplaced
