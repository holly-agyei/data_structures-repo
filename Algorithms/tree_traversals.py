#inorder--->left as you can, root(print), right.
#go left as u can till u hit, print it,  then recursively traverse the right of that same node, when the 
#the right is none, here the parent will will be printed.

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
#or
def inorder(root):
    stack = []
    results = []
    current =  root

    while True:
        if current:
            stack.append(current)
            current = current.left
        
        else:
            if not stack:
                return results #done
            current = stack.pop()
            results.append(current.val)
            current = current.right

def postoder(root):
  pass    
