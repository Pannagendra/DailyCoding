"""
You are given the head of a Singly linked list. You have to reverse every k node in the linked list and return the head of the modified list.
Note: If the number of nodes is not a multiple of k then the left-out nodes at the end, should be considered as a group and must be reversed.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        if not head or k <= 1:
            return head

        # Helper function to reverse a segment of the linked list
        def reverse_segment(start, end):
            prev, curr = None, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, start  # new head, new tail

        dummy = Node(0)
        dummy.next = head
        group_prev = dummy
        curr = head

        while curr:
            # Find the k-th node
            kth = curr
            count = 1
            while count < k and kth.next:
                kth = kth.next
                count += 1

            nxt_group = kth.next  # next group's head
            kth.next = None  # cut off group

            # Reverse current group
            new_head, new_tail = reverse_segment(curr, None)

            # Connect reversed group
            group_prev.next = new_head
            new_tail.next = nxt_group

            # Move pointers forward
            group_prev = new_tail
            curr = nxt_group

        return dummy.next
