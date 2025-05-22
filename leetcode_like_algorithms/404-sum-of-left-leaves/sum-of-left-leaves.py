# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #each node, explore it's left.
        self.summ = 0
        def dfs(node):
            if not node:
                return 
            

            if node.left and not node.left.left and not node.left.right:
                self.summ+=node.left.val
            dfs(node.left)
            dfs(node.right)
            
            return self.summ

        return dfs(root) 




        