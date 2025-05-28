# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        right_view = []
        queue = deque([root])

        while queue:
            size = len(queue)
            level_stack = []

            for _ in range(size):
                node = queue.popleft()
                level_stack.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            right_view.append(level_stack.pop())
        return right_view




