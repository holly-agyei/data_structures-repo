def merge(arr, low, mid, high):
    temp = []
    
    left = low
    right = mid+1
    
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left <= mid:
        temp.append(arr[left])
        left+=1
    while right <= high:
        temp.append(arr[right])
        right+=1
        
    for i in range(low, high+1):
        arr[i] = temp[i-low]
        
        
        


def mergesort(arr, low, high):
    #base case
    if low == high:
        return 
        
    #inductive case 
    
    mid = (low+high)//2
    
    mergesort(arr, low, mid)
    mergesort(arr, mid+1, high)
    merge(arr, low, mid, high)
    
arr = [3, 1, 2]
mergesort(arr, 0, len(arr) - 1)  # Call the function to sort the array
print(arr) 

