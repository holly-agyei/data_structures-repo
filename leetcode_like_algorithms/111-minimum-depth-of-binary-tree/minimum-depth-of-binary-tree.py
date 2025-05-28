# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            #for the base case, always imagine you have on root or a simple tree.
            if not node:
                return 0
            if not node.left: #go right only
                return 1+dfs(node.right)
            if not node.right:#go left only
                return 1+dfs(node.left)

            left= 1 + dfs(node.left)
            right = 1+dfs(node.right)

            return min(left, right)
        return dfs(root)


        