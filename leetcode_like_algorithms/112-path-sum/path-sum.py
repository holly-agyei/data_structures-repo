class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, curr_sum = stack.pop()

            # If it's a leaf node, check the sum
            if not node.left and not node.right and curr_sum == targetSum:
                return True

            # Add right first so left is processed first
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))

        return False


            
            

            

        return dfs(root, 0)
