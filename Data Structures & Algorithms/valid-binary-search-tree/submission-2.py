# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, node: TreeNode, low: int, high: int) -> bool:
        if not node:
            return True

        return low < node.val < high and self.validate(node.left, low, node.val) and self.validate(node.right, node.val, high)
