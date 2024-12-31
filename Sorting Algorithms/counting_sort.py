def countingsort(arr):
  """
  [3.3.2.1]
  algorithm to get the max 
  arr with values 0, max.
  to find the index: value -1
  [1,1,1]
  count and values
  
  arr = [1,2,3,3]
  
  """
  max = float("-inf")
  
  for value in arr:
      if value > max:
          max = value

  temp = [0]*max
  
  #loop over the arr and update their occurences in temp
  for value in arr:
      temp[value-1] +=1

  #LOOP OVER THE TEMP 
  final_array = []
  #[1,2,1]
  for i in range(len(temp)):
      for j in range(temp[i]):
          final_array.append(i+1)
  return final_array

arr = [3,1,2]
print(countingsort(arr))
          
