# so given any array we want to max heapify the array
# so any heap, has internal and leaf nodes
# the internal nodes start from 0 to n/2 -1 floor in 0 indexed array
# leaf nodes continue from n/2 floor to n-1. 

# to heapify any value at i, we need to make sure it's left and right nodes are already heapified
# to do this, start from sure last internal node to the first node and max heapify each i 

# So what we need to focus on is to get maxheapify(arr, i) function.

def max_heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    
    if left < len(arr) and arr[left]> arr[i]:
        large = left
    else:
        large = i
        
    if right <len(arr) and arr[right] > arr[large]:
        large = right
        
    if i != large:
        arr[i], arr[large] = arr[large], arr[i]
        max_heapify(arr, large)
        
# now let's call this maxheapify on every internal node starting from the last to the first.
def heapify_arr(arr):
    for i in range(int(len(arr)/2)-1, -1, -1): # the floor division can also be //  len(arr)//2 -1
        max_heapify(arr, i)
        
    return arr



print(heapify_arr([1,8,5,3,2]))


        
     