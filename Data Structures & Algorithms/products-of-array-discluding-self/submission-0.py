class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1] * size

        # Calculate prefix product
        prefix_product = 1
        for i in range(size):
            res[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(size-1, -1, -1):
            res[i] *= suffix_product
            suffix_product *= nums[i]

        return res
        