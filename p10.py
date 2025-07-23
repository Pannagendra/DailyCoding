"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

    Remove substring "ab" and gain x points.
        For example, when removing "ab" from "cabxbae" it becomes "cxbae".
    Remove substring "ba" and gain y points.
        For example, when removing "ba" from "cabxbae" it becomes "cabxe".

Return the maximum points you can gain after applying the above operations on s.
"""

class Solution(object):
    def maximumGain(self, s, x, y):
        def removeSubstring(string, first_char, second_char, points):
            """
            Remove all occurrences of first_char + second_char and return points gained
            """
            stack = []
            total_points = 0
            
            for char in string:
                # If we can form the target substring, remove it and gain points
                if stack and stack[-1] == first_char and char == second_char:
                    stack.pop()  # Remove the first character from stack
                    total_points += points
                else:
                    stack.append(char)
            
            return ''.join(stack), total_points
        
        # Greedy approach: always remove the higher value substring first
        if x >= y:
            # Remove "ab" first (worth x points), then "ba" (worth y points)
            remaining_string, points1 = removeSubstring(s, 'a', 'b', x)
            remaining_string, points2 = removeSubstring(remaining_string, 'b', 'a', y)
        else:
            # Remove "ba" first (worth y points), then "ab" (worth x points)
            remaining_string, points1 = removeSubstring(s, 'b', 'a', y)
            remaining_string, points2 = removeSubstring(remaining_string, 'a', 'b', x)
        
        return points1 + points2
