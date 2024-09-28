def second_largest(arr):
    """
    We are using the optimal solution in O(N)
    1. set the largest element to the first element
    2. set the second largest element to the min element
    3. loop through the array and perfome three different operations with conditions.

     """
    
    largest = arr[0]
    second_largest = float("-inf")
    
    for i in range(1,len(arr),1):

        if arr[i] == largest:
            continue
        
        elif arr[i] > largest and arr[i] > second_largest:
            largest = arr[i]
            second_largest = arr[i-1]      

        elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]      

    return largest, second_largest


