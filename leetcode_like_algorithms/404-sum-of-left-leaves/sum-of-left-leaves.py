class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        stack = [(root, False)]
        summ = 0

        while stack:
            node, is_left = stack.pop()

            # Check if it's a leaf
            if not node.left and not node.right and is_left:
                summ += node.val

            if node.right:
                stack.append((node.right, False))

            if node.left:
                stack.append((node.left, True))

        return summ
