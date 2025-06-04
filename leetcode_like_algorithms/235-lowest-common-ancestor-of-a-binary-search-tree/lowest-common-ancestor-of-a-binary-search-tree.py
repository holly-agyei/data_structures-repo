# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #this is more like depth first search
        #for bst the left is always less than the root and the right is greater than the right.
        #if the two values are greater than the current node we are on, (they are non the right)--push right
        #if the two are less than the current node, the will be at the left...go left.
        #if else that's the node(LCA) 
        #we want the coomon split point of betwwen two node....until we find, keep moving.(split point is where the
        #two nodes branches.)..if they are not branching, 

        if not root:
            return None
        stack = [root]

        while stack:
            top_node = stack.pop()

            if p.val > top_node.val and q.val>top_node.val:
                stack.append(top_node.right)
            elif p.val < top_node.val and q.val<top_node.val:
                stack.append(top_node.left)
            else: #this means one is greater and one is smaller or equal to the node:
                return top_node
            
            