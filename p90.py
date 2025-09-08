"""
You are given the head of a linked list. You have to sort the given linked list using Merge Sort.
"""

class Solution:
    def mergeSort(self, head):
        # Base case: if head is None or only one element, return head
        if head is None or head.next is None:
            return head

        # Helper to find middle of the linked list (Tortoise and Hare method)
        def getMiddle(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        # Helper to merge two sorted lists
        def merge(l1, l2):
            dummy = Node(0)
            tail = dummy
            while l1 and l2:
                if l1.data < l2.data:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 or l2
            return dummy.next

        # Find middle and split
        mid = getMiddle(head)
        next_to_mid = mid.next
        mid.next = None

        # Recursively sort both halves
        left = self.mergeSort(head)
        right = self.mergeSort(next_to_mid)

        # Merge the sorted halves
        return merge(left, right)
