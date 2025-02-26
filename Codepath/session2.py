"""
Understand->returning any number that's not the min or the max
M->array manipulation
Plan->get the min and the max, return any number that's not the min nor the max
I
R
E

def goldilocks_approved(nums):
    maximum = float("-inf")
    minimum = float("inf")
    
    if len(set(nums))<=2:
        return -1
    
    for num in nums:
        if num > maximum:
            maximum = num
        if num<minimum:
            minimum = num 
    
    
    for num in nums:
        if num != maximum and num!= minimum:
            return  num
nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))   
"""
def sum_of_digits(num):

    sum = 0

    while num > 0:

        sum += num % 10

        num = num // 10
    return sum   

num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(