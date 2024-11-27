#we want to build aprogram that return the maximum number from a max_heap.
#1. copy the first element(max element) into an a variabel
#2. take the last element to replace the first element and finally remove the last element( decrease array size by 1)
#3. max heapify the array with target as index 0. (buttom down)


    # first call the max heapify algorithm
def max_heapify(arr, i):
        left = 2*i+1
        right = 2*i+2
        
        if left < len(arr) and arr[left]> arr[i]:
            large = left
        else:
            large = i
        if right < len(arr) and arr[right] > arr[i]:
            large = right
            
        if i != large:
            arr[i], arr[large] = arr[large], arr[i]
            
            max_heapify(arr, large)
            
def return_max(arr):
        max = arr[0]   # first step 
        
        arr[0] = arr.pop(len(arr)-1) #second step
        
        max_heapify(arr, 0)
        
        return max
    
    
print(return_max([5,3,4,2]))
        
        