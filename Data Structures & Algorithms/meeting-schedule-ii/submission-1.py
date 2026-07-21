"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        max_count = 0
        start,end,count = 0,0,0
        start_times = sorted([x.start for x in intervals])
        end_times = sorted([x.end for x in intervals])
        while start<n and end<n:
            if start_times[start]<end_times[end]:
                count += 1
                start += 1
            else:
                count -= 1
                end += 1
            max_count = max(max_count,count)
        return max_count
