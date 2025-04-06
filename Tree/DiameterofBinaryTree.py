# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        res = 0
        def dfs(root):
            if not root:
                return 0
            right = dfs(root.right)
            left = dfs(root.left)
            nonlocal res
            res = max(res,right+left)
            return 1 + max(right,left)
        dfs(root)
        return res