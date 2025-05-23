class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        stackL = [root.left]
        stackR = [root.right]

        while stackL and stackR:
            nodeL = stackL.pop()
            nodeR = stackR.pop()

            if not nodeL and not nodeR:
                continue
            if not nodeL or not nodeR:
                return False
            if nodeL.val != nodeR.val:
                return False

            # Push children in mirrored order
            stackL.append(nodeL.left)
            stackL.append(nodeL.right)

            stackR.append(nodeR.right)
            stackR.append(nodeR.left)

        # Both should be empty at the end
        return not stackL and not stackR
