# def maxdepth(root):
#     if not root:
#         return 0
#     left = maxdepth(root.left)
#     right = maxdepth(root.right)
    
#     return 1+max(left, right)

# #or
# def maxdepth(root):
#     stack = [(root,1)]
#     max_depth = 0

#     while stack:
#         node, depth = stack.pop()
        #update the maxdepth here
#         if node:# thus if node is not None, prolly, we wont handle Null here
#             stack.append(root.right, depth+1)
#             stack.append(root.left, depth+1)
#     return max_depth


