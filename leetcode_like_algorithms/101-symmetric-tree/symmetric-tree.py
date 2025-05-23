# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(right, left):
           if not left and not right:
                return True #meaning we ended without any difference in nodes
           if not left or not right: 
                return False
           if left.val != right.val:
                return False
            
           return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)

        #iterarative:
        #store the right and left subtress into two different stacks using preorder traversal        #just compare nodes.


        