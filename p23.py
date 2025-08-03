"""
Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts amounti fruits at the position positioni. fruits is already sorted by positioni in ascending order, and each positioni is unique.

You are also given an integer startPos and an integer k. Initially, you are at the position startPos. From any position, you can either walk to the left or right. It takes one step to move one unit on the x-axis, and you can walk at most k steps in total. For every position you reach, you harvest all the fruits at that position, and the fruits will disappear from that position.

Return the maximum total number of fruits you can harvest.
"""
class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        # Extract positions and prefix sums
        n = len(fruits)
        pos = [fruits[i][0] for i in range(n)]
        amount = [fruits[i][1] for i in range(n)]
        # prefix[i] = sum of amount[0:i]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + amount[i]
        
        ans = 0
        left = 0
        for right in range(n):
            # Window from fruits[left][0] to fruits[right][0]
            while left <= right:
                l = pos[left]
                r = pos[right]
                # Calculate minimum steps needed to visit all in [l, r]
                # To cover [l, r], start at startPos, go to l or r first, then to the other end
                need = min(abs(startPos - l), abs(startPos - r)) + (r - l)
                if need <= k:
                    break
                left += 1
            # If valid, update answer
            if left <= right:
                ans = max(ans, prefix[right+1] - prefix[left])
        return ans
