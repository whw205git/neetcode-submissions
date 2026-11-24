# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        low, high = min(p.val, q.val), max(p.val, q.val)

        curr = root
        while curr:
            # If both are strictly higher than current node's value, it's in the right subtree        
            if low > curr.val:
                curr = curr.right
            # If both are strictly lower than current node's value, it's in the left subtree        
            elif high < curr.val:
                curr = curr.left
            # Current node is the lowest common ancestor
            else:
                return curr

        return None
        