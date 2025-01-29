"""
def check_pairs(s)->str:
    stack = []
    pairs = {'(':')','{':'}','[':']'}

    for char in s:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if stack and pairs[stack[-1]] == char:
                stack.pop()
            else:
                return False
    return not stack

s = "(([]){"
print(check_pairs(s))

"""
"""

stack = []
min_stack = []

def push(element):
    
       min_stack.append(element)
    elif element <= min_stack[-1]:
            min_stack.append(element)
            stack.append(element)
    else:
        stack.append(element)


def pop():
    if stack:  # Check if the stack is not empty
        if stack[-1] == min_stack[-1]:  # Check if the top element is the current minimum
            min_stack.pop()  # Remove it from min_stack
        return stack.pop()  # Return the popped element
    else:
        return None  # Handle empty stack case
    
   
def top():
    if stack:
        print((stack[-1]))
    else:
        return None
    

def getMin():
    if min_stack:
        print((min_stack[-1]))
    else:
        return None


   


push(3)
push(5)
getMin()
push(2)
getMin()
push(1)
getMin()
pop()
getMin()
pop()
pop()
getMin()

"""

"""
def remove_dupes(items):
   start = 0
   end = len(items)-1

   while start < len(items)-1:
      if items[start]==items[end]:
         del items[end]
         end -=1
         start +=1
      else:
        end -=1

   return len(items)



items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))
        

        """

"""
Given an integer array nums, write a function sort_by_parity() that moves all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""
start = 0
end = 0

def sort_by_parity(nums):
    
    start = 0
    end = len(nums)-1

    while start < end:
        #when the first is even and the last is odd
        if nums[start]%2==0 and nums[end]%2 == 1:
            start +=1
        elif nums[start]%2==1 and nums[end]%2 == 0:
            nums[start], nums[end] = nums[end], nums[start]
            start +=1
            end -=1
        elif nums[start]%2==1 and nums[end]%2 == 1:
            end -=1
        else:
            start +=1
    return nums





nums =[3,1,2,4,9,6,8,10,4]
print(sort_by_parity(nums))




     
    





        