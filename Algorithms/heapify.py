def max_heapify(arr, i):
    # this is going to be a recursive function.
    # we start from the ith element that destroys the heap structure and perform the compare-swap operation
    
    # we stop when i is at a leaf node or i is greater it's L AND R children
    #to check when i is at leaf, I wont contain left or right child. so L and R will go out of bound.
    #call the recursive function when the largest of i and it's children is one of it's children.( i less than one of the children, we swap)
    
    left, right = 2*i+1, 2*i+2
    
    
    #first condition 
    if left < len(arr) and arr[left] > arr[i]:
        largest = left
    else:
        largest = i
        
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right
        
    # now assume we have gotten the largest between the r, l and i
    if largest != i:  # this if largest is anything else
        #swap
        arr[i], arr[largest] = arr[largest], arr[i]
        
        #after the swap, call the recursive function, this time, our point of focus is the 
        
        
        max_heapify(arr, largest)
        
    # this is an in-place function and we dont need to return the arr, instead, the array is directly modified!
        
print(max_heapify([1,2,3], 0))


        
    