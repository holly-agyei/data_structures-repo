#imagine you have a heap and you want to increase the one of the values! 
#well, after increasing the value at any given index, it may destroy the heap property and you will have to re-organise the heap.

#1. update the value with the key given
# for max hap, check if the key is greater than its parent, if so, we need to percolate up!
#How do we percolate up? 
    #you end when the arr[i] < its parent arr[i/2-1]---floor or i/2 ceil -1. 
    #or when i is at the root node. i = 0  
# Always be careful about the parent fomula 
# it is ceil(i/2)-1 or floor((i-1)/2) same as (i-1)//2 .....stick to one
def increase_key(arr, i, key):
    arr[i] = key # assign key to the index
    if arr[i] < arr[int((i-1)//2)]:
        return arr
    
    while i > 0 and arr[i] > arr[int(i/2)]:
        arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
        
        # here is the crucial step, now after the swap, assign, value at i takes the index at the parent(i/2)-1 floor
        i = (i-1)//2
    return arr
print(increase_key([7,5,4,2,3], 4, 10))
    

