class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []

        def dfs(idx: int):
            if idx >= len(nums):
                results.append(subset.copy())
                return

            # include current number
            subset.append(nums[idx])
            dfs(idx + 1)

            # do not include current number
            subset.pop()
            dfs(idx + 1)

        dfs(0)
        return results
        