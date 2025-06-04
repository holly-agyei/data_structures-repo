#inorder--->left as you can, root(print), right.

def inorder(root):
    stack = []
    results = []
    current =  root

    while current or stack:
        #go left
        while current:
            stack.append(current)
            current = current.left

        #print after getting a Null
        current = stack.pop()
        results.append(current.val) #root

        #right
        current = current.right


