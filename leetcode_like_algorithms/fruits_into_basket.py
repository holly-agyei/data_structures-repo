class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        create a set to store two max elements
        create a max_count and curr_count 
        create a last occurrence variable = 0
        

        while right pointer in the array:

            

            1.if set <  and element not in set:
                add element 
                increase window
                curr_count+=1                
                max = max(max, r-l+1)
                 
          2. if element in set:
                
                max = max(max, r-l+1)
                
            
            3. if element not in set:
                move the left to the last occurence
                remove from the set which is not the last occurence
                add the element to set

                max = max(max, r-l)
                increase window 
                
 

            if arr[i-1] != arr[lst] 
            lastoccurrence = i-1
                
             """
        if not fruits:
            return 0

        hashh = set()
        max_count, lastOcurr, right, left  = 0, 0, 0, 0

        while right < len(fruits):
            if fruits[right] not in hashh and len(hashh) <2:
                hashh.add(fruits[right])
                max_count = max(max_count, right-left+1)
                right +=1
                
            elif fruits[right] in hashh:
                max_count = max(max_count, right-left+1)
                right+=1
                
            
            elif fruits[right] not in hashh and  len(hashh)==2:
                
                
                #remove one from the set which is not the last occurence
                for i in hashh.copy():    #you cant itereate and modify set at the same time
                    if i != fruits[lastOcurr]:
                        hashh.remove(i)
                hashh.add(fruits[right])

                #bring
                left = lastOcurr
                max_count = max(max_count, right-left+1)  # cos in this case, right is one ahead of the last valid window
                right+=1

            
            #update the last occurence
            if fruits[right-1] != fruits[lastOcurr]:
                lastOcurr = right-1
        #return answer
        print(left, right, lastOcurr)
        return max_count
    
    
    #




                
                





            
            
            



        