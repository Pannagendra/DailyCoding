"""
You are given two arrays mices[] and holes[] of the same size. 
The array mices[] represents the positions of the mice on a straight line, while the array holes[] represents the positions of the holes on the same line. 
Each hole can accommodate exactly one mouse. A mouse can either stay in its current position, move one step to the right, or move one step to the left, 
and each move takes one minute.
The task is to assign each mouse to a distinct hole in such a way that the time taken by the last mouse to reach its hole is minimized.

Input: mices[] = [4, -4, 2], holes[] = [4, 0, 5] 
Output: 4
Explanation: Assign the mouse at position 4 to the hole at position 4, so the time taken is 0 minutes. 
Assign the mouse at position −4 to the hole at position 0, so the time taken is 4 minutes. 
Assign the mouse at position 2 to the hole at position 5, so the time taken is 3 minutes. Hence, the maximum time required by any mouse is 4 minutes.
"""
class Solution:
    def assignHole(self, mices, holes):
        mices.sort()
        holes.sort()
        return max(abs(m - h) for m, h in zip(mices, holes))



