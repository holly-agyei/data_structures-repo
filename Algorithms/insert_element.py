def insert(arr, key):
    # add to the last element
    arr.append(key)
    
    i = len(arr)-1
    
    while i > 0 and arr[i] > arr[(i-1)//2]:
        arr[i], arr[(i-1)//2] =arr[(i-1)//2], arr[i]
        
        i = (i-1)//2
        
    return arr

arr = [3,2,1]

print(insert(arr, 4))
        
        
        
        
        
    







   