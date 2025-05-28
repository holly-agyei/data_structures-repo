# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #we can also use bfs, just stop at level that one of the childs seems missing.
        level = 0
        que = deque([root])

        if not root:
            return 0
        while que:
            size = len(que)
            level+=1
            
            for _ in range(size):
                node = que.popleft()

               
                   
                if not node.right and not node.left:
                    return level
                    
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)









        