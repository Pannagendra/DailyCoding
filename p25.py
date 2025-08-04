"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
"""
from collections import defaultdict, deque

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        # Dictionary to store the nodes at each column index
        col_table = defaultdict(list)
        # Queue for BFS: store pairs of (node, column_index)
        queue = deque([(root, 0)])
        
        min_col = max_col = 0
        
        while queue:
            node, col = queue.popleft()
            if node:
                col_table[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                # Left child goes to col - 1
                if node.left:
                    queue.append((node.left, col - 1))
                # Right child goes to col + 1
                if node.right:
                    queue.append((node.right, col + 1))
        
        # Extract the columns from leftmost to rightmost
        result = []
        for c in range(min_col, max_col + 1):
            result.append(col_table[c])
        
        return result
