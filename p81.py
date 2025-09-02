"""
Given the head of a singly linked list and an integer k. Swap the kth node (1-based index) 
from the beginning and the kth node from the end of the linked list. 
Return the head of the final formed list and if it's not possible to swap the nodes return the original list.

Count the length n of the list.

If k > n, return head (swap not possible).

If 2*k - 1 == n, it means both nodes are the same → return head.

Find the kth node from start (x) and kth node from end (y).

y is the (n-k+1)th node from start.

Swap their data (simplest way).
"""
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def swapKth(self, head, k):
        # Step 1: find length of the list
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        
        # Step 2: if k is more than length, return unchanged
        if k > n:
            return head
        
        # Step 3: if kth node from start and end are same
        if 2*k - 1 == n:
            return head
        
        # Step 4: find kth node from start
        first = head
        for _ in range(k - 1):
            first = first.next
        
        # Step 5: find kth node from end (n-k+1 th node from start)
        second = head
        for _ in range(n - k):
            second = second.next
        
        # Step 6: swap the data
        first.data, second.data = second.data, first.data
        
        return head
