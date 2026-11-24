class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end
        intervals.sort(key=lambda x:x[1])

        prev = intervals[0]
        removed = 0
        # always keep the smallest end if the intervals are overlapping
        for curr in intervals[1:]:
            if curr[0] < prev[1]:
                removed += 1
            else:
                prev = curr
        
        return removed

        