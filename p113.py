"""
You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.
"""
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """
        Find the maximum number of minutes you can run all n computers simultaneously.
        
        Strategy: Binary search on the answer.
        For a given time t, check if we can run all n computers for t minutes.
        
        Key insight: Each battery can contribute at most min(battery, t) minutes
        in a time window of t minutes.
        """
        # Binary search range: 0 to average battery capacity
        left, right = 0, sum(batteries) // n
        
        def canRun(time):
            """Check if we can run all n computers for 'time' minutes"""
            # Total available power for running n computers for 'time' minutes
            # Each battery can contribute at most min(battery, time) minutes
            total_power = sum(min(battery, time) for battery in batteries)
            
            # We need n * time total minutes of power
            return total_power >= n * time
        
        # Binary search for the maximum valid time
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if canRun(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
