#first define a partition algorithm
#all element greater than the pivot are to the right and all elements less than the pivot are to the left 
#swap the pivot element to the ith position

def partition(arr, l, r):
    
    i= l
    
    for j in range(l, r):
        if arr[j]<= arr[r]:
            #swap
            arr[i], arr[j] = arr[j], arr[i]

            i+=1
    arr[i], arr[r] = arr[r], arr[i]

    return i 

def quickselect(arr, l, r, k):
    i = partition(arr,l,r)
    
    if k-1 == i:
        return arr[i]
    elif k-1 <i:
        return quickselect(arr, l, i-1,k)
    else:
        return quickselect(arr, i+1, r,k)
    
    

print(quickselect([1,3,5,2],0,3,3))
        