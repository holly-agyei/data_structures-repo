def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2 
    
    if left < len(arr) and arr[left] > arr[i]:
        large = left
    else:
        large = i 
    if  right < len(arr) and arr[right] > arr[large]:
        large = right
    
    if i != large:
        arr[i], arr[large] = arr[large], arr[i]
        heapify(arr, large)
        

def max_heapify(arr):
    for i in range(int(len(arr)/2)-1, -1, -1): # the floor division can also be //  len(arr)//2 -1
        heapify(arr, i)
    return arr

print(max_heapify([1,8,5,3,2]))
        
sum = 0
total = sum 
total = 4

print(sum)