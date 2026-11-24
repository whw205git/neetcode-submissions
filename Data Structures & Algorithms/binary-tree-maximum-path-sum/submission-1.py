# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')

        def dfs(node: Optional[TreeNode]):
            nonlocal max_path_sum

            if not node:
                return 0

            # calculate max gain from the left path and right path. If negative, set at 0
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            # calculate sum of a path from left to right through current node
            current_path_sum = left_gain + node.val + right_gain

            # take the max
            max_path_sum = max(max_path_sum, current_path_sum)

            # max that the node can contribute to the parent is either through the left path or the right path
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return max_path_sum
        