# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []#empty then
        queue = deque([root])
        results, left_to_right =[], True

        while queue:
            
            size = len(queue)
            level = [0]*size

            for i in range(size):
                node = queue.popleft()
                
                if left_to_right:
                    level[i] = node.val
                else:
                    level[size-i-1] = node.val #append from the left

                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(level)
            left_to_right = not left_to_right
            
        return results
            
                




        

        