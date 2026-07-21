class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        end = intervals[0][1]
        remove_count = 0
        for interval in intervals[1:]:
            if interval[0]>=end:
                end = interval[1]
            else:
                remove_count += 1
        return remove_count