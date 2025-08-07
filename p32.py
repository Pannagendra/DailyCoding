"""
Given an array arr[] of time strings in 24-hour clock format "HH:MM:SS", return the minimum difference in seconds between any two time strings in the arr[].
The clock wraps around at midnight, so the time difference between "23:59:59" and "00:00:00" is 1 second.
"""
class Solution:
    def minDifference(self, arr):
        from datetime import datetime

        # Helper to convert "HH:MM:SS" to total seconds from midnight
        def time_to_seconds(t):
            dt = datetime.strptime(t, "%H:%M:%S")
            return dt.hour * 3600 + dt.minute * 60 + dt.second
        
        times_in_seconds = sorted(time_to_seconds(t) for t in arr)
        min_diff = float('inf')
        n = len(times_in_seconds)
        
        for i in range(1, n):
            # Difference between consecutive times
            diff = times_in_seconds[i] - times_in_seconds[i-1]
            if diff < min_diff:
                min_diff = diff
        
        # Also consider wrap-around difference between last and first time
        wrap_diff = 24 * 3600 - times_in_seconds[-1] + times_in_seconds[0]
        if wrap_diff < min_diff:
            min_diff = wrap_diff
        
        return min_diff
