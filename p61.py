"""
Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

    Each student receives atleast one book.
    Each student is assigned a contiguous sequence of books.
    No book is assigned to more than one student.

The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

Note: If it is not possible to allocate books to all students, return -1.
"""
class Solution(object):
    def isPossible(self, arr, n, k, mid):
        students = 1
        pages = 0
        for i in range(n):
            if arr[i] > mid:
                return False
            if pages + arr[i] > mid:
                students += 1
                pages = arr[i]
                if students > k:
                    return False
            else:
                pages += arr[i]
        return True

    def findPages(self, arr, k):
        n = len(arr)
        if n < k:  # not enough books
            return -1
        
        low = max(arr)
        high = sum(arr)
        res = -1

        while low <= high:
            mid = (low + high) // 2
            if self.isPossible(arr, n, k, mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
