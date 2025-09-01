""".
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.


🔹 Greedy Algorithm Explanation
Problem Restated

We want to maximize the average pass ratio after distributing extraStudents.
Each time we add one student to a class, that class’s pass ratio increases.

👉 The key insight:
Not all classes benefit equally from adding a student.
So, we must always give the next student to the class where the increase (gain) is the biggest.

This is a classic greedy choice problem:

At each step, pick the option that gives the most immediate improvement.

Repeat until no extra students remain.

Pass Ratio Gain Formula

If a class has:

p passing students

t total students

Then:

Current ratio = p / t

Ratio after adding 1 student = (p+1) / (t+1)

So the gain is:

Δ=t+1/p+1−t/p
	​


This tells us how much benefit we get if we assign 1 student to this class.

Why Greedy Works Here

Each extra student affects only one class.

The gain from adding a student is always positive but decreasing (adding the first student helps more than adding the 10th).

So, the best strategy is always to assign the student to the class with the biggest immediate gain.

This is why greedy works → because the local best choice leads to the global maximum.
"""
import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Function to compute gain if we add one student
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t
        
        # Build a max-heap (store negative because Python's heapq is min-heap)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)
        
        # Assign extra students one by one
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1   # add student
            heapq.heappush(heap, (-gain(p, t), p, t))
        
        # Calculate final average
        total_ratio = sum(p / t for _, p, t in heap)
        return total_ratio / len(classes)
