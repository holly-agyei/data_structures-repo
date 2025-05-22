# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = None
            
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
       
        
       
        

        def dfs(node, val):
            if not node:
                return 
            
            if node.val == val:
                self.ans = node
                return
            
            dfs(node.right, val)
            dfs(node.left, val)

        dfs(root, val)
        return self.ans

                
        