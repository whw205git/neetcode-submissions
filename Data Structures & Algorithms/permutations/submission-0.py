class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(perm: List[int], picked: List[bool]):
            if len(perm) == len(nums):
                results.append(perm.copy())
                return

            for i in range(len(nums)):
                if not picked[i]:
                    num = nums[i]
                    perm.append(num)
                    picked[i] = True
                    backtrack(perm, picked)
                    perm.pop()
                    picked[i] = False
        
        backtrack([], [False]*len(nums))
        return results