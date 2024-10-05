"""
Given an array, Move all the zero's to the array. 
Solution
-set two pointers
point the first to the first zero in the array
if there's is no zero, then just return the array
point the second pointer next to the first pointer
loop through using the second pointer and perform a couple of swaps

"""
def move_zeros_to_end(arr):
    j = None
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
        break
    if j == None:
        return arr
    
    #now i = j+1 
    for i in range(j+1, len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]   #SWAP using tuple unpacking, where values are stored temporarily.
            j +=1    #make sure j is always pointed to the zero
    return arr

print(move_zeros_to_end([0,2,3,0,9,3,4,0,3,0,0,0,4]))
#output = [2, 3, 9, 3, 4, 3, 4, 0, 0, 0, 0, 0, 0]










