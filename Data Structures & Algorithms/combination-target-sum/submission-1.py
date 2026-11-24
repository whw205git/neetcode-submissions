class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort for short circuit
        nums.sort()
        results = []
        combination = []

        def dfs(idx: int, remaining: int):
            if idx == len(nums):
                return

            for i in range(idx, len(nums)):
                num = nums[i]

                # Since it's sorted, if over target we do not need to proceed
                if num > remaining:
                    break

                combination.append(num)
                if num == remaining:
                    results.append(combination.copy())
                else:
                    dfs(i, remaining - num)
                combination.pop()

        dfs(0, target)
        return results