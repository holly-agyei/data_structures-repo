# define the quicksort function
def quicksort(arr):

    # set base case
    """
    This uses the Divide and conquer strategy
    if len(arr) is 0 or 1, it returns the array
    """
    if len(arr) <= 1:
        return arr
    else:

        #set a pivot, in this case using the first element or index.
        pivot = arr[0]
        
        # find all elements less than the pivot
        less = [i for i in arr[1:] if i < pivot]

        # find all elements greater than the pivot
        greater = [ i for i in arr[1:] if i > pivot]

        #Set the inductive case
        arr =  quicksort(less) + pivot + quicksort(greater)
        return arr
        
        
        
