"""
There are n gas stations along a circular tour. 
You are given two integer arrays gas[] and cost[], where gas[i] is the amount of gas available at 
station i and cost[i] is the gas needed to travel from station i to station (i+1). 
You have a car with an unlimited gas tank and start with an empty tank at some station. 
Your task is to return the index of the starting station if it is possible to travel once around the circular route 
in a clockwise direction without running out of gas at any station; otherwise, return -1.

Note: If a solution exists, it is guaranteed to be unique.
"""
class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        
        total, tank, start = 0, 0, 0
        for i in range(n):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            
            # If tank < 0, reset starting point
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start if total >= 0 else -1
