"""
Given the head of a linked list where nodes can contain values 0s, 1s, and 2s only.
Your task is to rearrange the list so that all 0s appear at the beginning, followed by all 1s, and all 2s are placed at the end.
"""
class Solution:
    def segregate(self, head):
        if head is None or head.next is None:
            return head
        
        # Count number of 0s, 1s, and 2s
        count = [0, 0, 0]
        current = head
        while current:
            count[current.data] += 1
            current = current.next
        
        # Modify the linked list based on counts
        current = head
        for i in range(3):
            while count[i] > 0:
                current.data = i
                current = current.next
                count[i] -= 1
        return head
