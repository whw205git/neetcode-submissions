class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start, then by end
        sorted_intervals = sorted(intervals)

        prev = sorted_intervals[0]
        removed = 0
        # always keep the smallest end if the intervals are overlapping
        for curr in sorted_intervals[1:]:
            if curr[0] < prev[1]:
                removed += 1
                if curr[1] < prev[1]:
                    prev = curr
            else:
                prev = curr
        
        return removed

        