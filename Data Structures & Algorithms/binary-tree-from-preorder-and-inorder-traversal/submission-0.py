# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        self.preorder_idx = 0

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            root_val = preorder[self.preorder_idx]
            node = TreeNode(root_val)
            self.preorder_idx += 1

            mid = inorder_index_map[root_val]
            node.left = helper(left, mid-1)
            node.right = helper(mid+1, right)

            return node

        return helper(0, len(preorder)-1)

        