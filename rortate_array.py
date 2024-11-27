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


"""
given an array, rotate it to the right by d elements.

Solution
-reverse from -dth element to the last element. 
-reverse from first element  (len(arr)-d)th element
-reverse the the whole array

"""
def rotate_array_right(arr,d):
        #Handle cases where d is larger than the size of the array
        d = d%len(arr)
        n = len(arr) 

        arr = arr[(n-1)-d::-1]+ arr[:(n-1)-d:-1] 
        return arr[::-1]
                                                                                                