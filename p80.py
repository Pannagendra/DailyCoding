"""
Given an array arr[] of positive integers and an integer k. You have to find the sum of the modes of all the subarrays of size k.
Note: The mode of a subarray is the element that occurs with the highest frequency. If multiple elements have the same highest frequency, the smallest such element is considered the mode.

🔹 Problem Reminder

We need to find the mode of every subarray of size k in arr[], then sum them all up.

Naive way:

For each subarray, recalculate frequency from scratch → O(n*k) → too slow when n, k are large.

👉 Instead, we use sliding window.

🔹 What is Sliding Window?

Sliding window is a technique where you maintain information about a fixed-size segment (window) of an array, and instead of recomputing everything when the window moves, you just update the difference (remove one element, add another).

🔹 How it works in this problem

Say: [1,2,2,3] , k =3
Step 1: First Window

Take first k elements → [1, 2, 2].

Build frequency map: {1:1, 2:2}.

Mode = 2.

Step 2: Slide to Next Window

Now the window moves one step right: [2, 2, 3].

Outgoing element = 1 (leftmost of old window).

Incoming element = 3 (new element entering).

Instead of recomputing everything:

Decrease count of 1.

Increase count of 3.

So now frequency map becomes {2:2, 3:1}.

Mode = 2.

Step 3: Repeat

Keep sliding until the end of the array.

Each time:

Remove one element (decrement count in map).

Add one element (increment count in map).

Then get the mode efficiently (using a heap or ordered structure).

🔹 Why Sliding Window Helps

Naive: For each window, build freq map from scratch → O(k).

Sliding window: Only 2 updates per step (outgoing + incoming) → O(1).

Finding the mode:

With heap → O(log k).

So total = O(n log k).

Much faster and passes time limits.





Optimized Approach

Maintain:

freq: dictionary → element → count.

max_heap: max-heap of (-frequency, value).

Negative frequency since Python has min-heap.

Store ( -count, value ) so that ties are broken by smaller value automatically.

For each window:

Push updated ( -freq[val], val ) into heap when a value changes.

The heap may contain old (outdated) entries, so before using the top, we pop until it matches current freq.

This gives us the correct mode in O(log k).

Sliding window update:

Decrease count of outgoing element.

Increase count of incoming element.

Push new states into heap.
"""
import heapq
from collections import defaultdict

class Solution:
    def sumOfModes(self, arr, k):
        n = len(arr)
        if k > n:
            return 0
        
        freq = defaultdict(int)
        heap = []  # stores (-count, value)
        
        # initialize first window
        for i in range(k):
            freq[arr[i]] += 1
        for val, cnt in freq.items():
            heapq.heappush(heap, (-cnt, val))
        
        def get_mode():
            # pop until top of heap is consistent with freq map
            while heap:
                cnt, val = heap[0]
                if -cnt == freq[val]:
                    return val
                heapq.heappop(heap)
            return 0  # shouldn't happen
        
        total_sum = get_mode()
        
        # slide the window
        for i in range(k, n):
            # outgoing
            out = arr[i-k]
            freq[out] -= 1
            heapq.heappush(heap, (-freq[out], out))
            
            # incoming
            incoming = arr[i]
            freq[incoming] += 1
            heapq.heappush(heap, (-freq[incoming], incoming))
            
            total_sum += get_mode()
        
        return total_sum
