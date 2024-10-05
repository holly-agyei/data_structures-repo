"""
given an array, rotate it to the left by d elements.

Solution
-reverse from the first index to the d-1th index
-reverse from dth index to the last element
-reverse the the whole array

"""
def rotate_array(arr,d):
        #Handle cases where d is larger than the size of the array
        d = d%len(arr)
      
        arr = arr[d-1::-1]+arr[:d-1:-1] 
        return arr[::-1]