# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        #get each row using bfs
        #find the max and append res
        if not root:
            return []
        tree = deque([root])
        res = []

        while tree:
            level_len = len(tree)
            highest = 0
            
            for i in range(level_len):
                node = tree.popleft()
                if i == 0:
                    highest = node.val
                else:
                    highest = max(node.val, highest)

                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
                
            res.append(highest)
        return res




