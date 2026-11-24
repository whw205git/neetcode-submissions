class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        extended_heights = heights + [0]

        for i, curr_height in enumerate(extended_heights):
            while stack and curr_height < extended_heights[stack[-1]]:
                prev_height = extended_heights[stack.pop()]
                area = prev_height * (i if not stack else i - stack[-1] - 1)
                max_area = max(area, max_area)
            stack.append(i)

        return max_area

        