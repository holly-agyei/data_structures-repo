"""
Given two SORTED arrays, find the union

solution:
1. use two pointers, i for the first array and j for the second array
2. use wile loop:while j and i are within the loops
3. if i is less than j, and if i is not in union, append i and increase the pointer regardless
4. perform similar fuction for j

6. after one size is exhausted, append the elements in the rest of the other array provided they are not in the union.
O(n+m)
"""
# define the function
def find_union(arr1, arr2):
    union = []
    i, j = 0,0

    while i < len(arr1) and j < len(arr2):
        #start looping while creating the conditions
        if arr1[i] <= arr2[j]:
            if len(union) == 0 or arr1[i] != union[-1]:
                union.append(arr1[i])
            i +=1
        # Check The same condition for arr2 and j
        else:
            if len(union) == 0 or arr2[j] != union[-1]:
                union.append(arr2[j])
            j +=1
    
    while j < len(arr2):
        if arr2[j] != union[-1]:
            union.append(arr2[j])
        j += 1
    
    while i < len(arr1):
        if arr1[i] != union[-1]:
            union.append(arr1[i])
        i +=1

    return union

arr1, arr2 = [1,2,3,4,5,6], [1,3,5,7,8,9]

print(find_union(arr1,arr2))
