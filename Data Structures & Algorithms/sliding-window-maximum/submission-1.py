from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()

        for i, num in enumerate(nums):
            # Remove numbers out of bounds from the front of queue
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # If a new element entering the window is greater, remove the older elements from the back of the queue
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # Add index to end of queue
            dq.append(i)

            # Front of queue is always the max element
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result