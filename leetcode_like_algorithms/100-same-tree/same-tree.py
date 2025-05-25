# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        #if you put the same binary tree into a stack using a pre-order traversal, the are the same:
        p_stack = [p]
        q_stack = [q]

        if not p and not q:
            return True
        if not p or not q:
            return False

        while p_stack or q_stack:
            p_node = p_stack.pop()
            q_node = q_stack.pop()

           
            if not p_node and not q_node:
                continue
            if not p_node or not q_node:
                return False

            if p_node.val != q_node.val:
                return False
            
            
            p_stack.append(p_node.right)
            p_stack.append(p_node.left)

                        
            q_stack.append(q_node.right)
            q_stack.append(q_node.left)
                        
            
               
        return True


        