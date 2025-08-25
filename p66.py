"""
Given a binary tree, convert the binary tree to its Mirror tree.

Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged.  
"""
'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def mirror(self, root):
        if root is None:
            return
        
        # Recursively mirror left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
        
        # Swap left and right children
        root.left, root.right = root.right, root.left
