"""
You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

Count the number of pairs of points (A, B), where

    A is on the upper left side of B, and
    there are no other points in the rectangle (or line) they make (including the border).

Return the count.

Brute force method,

Early filtering (if i == j or not (...) continue)

Avoids expensive inner checks for pairs that obviously don’t meet the geometric relation. This small check drastically reduces wasted work.

Triple loop brute-force

Simple and correct for modest n. It directly encodes the problem statement: for each ordered pair (A,B) that satisfies position constraint, verify no other point lies in the inclusive rectangle. Very readable and easy to reason about.

Inclusive rectangle (>=/<=)

The code treats points on the rectangle border as inside (they invalidate the pair). That matches "including the border" semantics you mentioned earlier.

n == 2 special case

Micro-optimization and clarity: when there are only two points, there's no third point to block, so valid pairs are counted instantly.

Early break when illegal

Once a block is found, there’s no need to check other points; this saves time and is standard practice.

Counts ordered pairs

Because loops go over all (i,j), the code counts ordered pairs. If A and B are swapped and still satisfy the condition, both would be considered separately. (If you intended unordered pairs, you’d change iteration to avoid double counting.)
"""

from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)

        for i in range(n):
            pointA = points[i]
            for j in range(n):
                pointB = points[j]
                if i == j or not (
                    pointA[0] <= pointB[0] and pointA[1] >= pointB[1]
                ):
                    continue
                if n == 2:
                    ans += 1
                    continue

                illegal = False
                for k in range(n):
                    if k == i or k == j:
                        continue

                    pointTmp = points[k]
                    isXContained = (
                        pointTmp[0] >= pointA[0] and pointTmp[0] <= pointB[0]
                    )
                    isYContained = (
                        pointTmp[1] <= pointA[1] and pointTmp[1] >= pointB[1]
                    )
                    if isXContained and isYContained:
                        illegal = True
                        break
                if not illegal:
                    ans += 1
        return ans
