# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #besst to try recursive today and do iterative tommorow
        max_d = 0
        def dfs(node):
            nonlocal max_d
            if not node:
                return 0
            #you want to go left and right fo each node and cal the dimaeter
            left = dfs(node.left)
            right=  dfs(node.right)
            max_d = max(max_d, left+right) #it will cal the max at each node, not only from the root

            return 1+max(left, right)

        dfs(root)
        return max_d


