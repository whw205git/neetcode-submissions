class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by first element
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        # merge if curr[start] < prev[end]
        prev = sorted_intervals[0]
        res = [prev]
        for curr in sorted_intervals[1:]:
            if curr[0] <= prev[1]:
                prev[1] = max(curr[1], prev[1])
            else:
                res.append(curr)
                prev = curr

        return res

        