"""
Geek has an array of non-overlapping intervals intervals[][] where intervals[i] = [starti , endi] represent the start and the
end of the ith event and intervals is sorted in ascending order by starti . 
He wants to add a new interval newInterval[] = [newStart, newEnd] where newStart and newEnd represent the start and end of this interval.
Help Geek to insert newInterval into intervals such that intervals is still sorted in 
ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
"""
class Solution:
    def insertInterval(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)
        
        # Add all intervals that end before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge all overlapping intervals with newInterval
        start = newInterval[0]
        end = newInterval[1]
        
        while i < n and intervals[i][0] <= newInterval[1]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        
        result.append([start, end])
        
        # Add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
