# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current_node = root

        while current_node or stack:
            while current_node:
                # Traverse to the leftmost node
                stack.append(current_node)
                current_node = current_node.left
                
            current_node = stack.pop()

            k -= 1
            if k == 0:
                return current_node.val
                
            current_node = current_node.right

        return -1

        