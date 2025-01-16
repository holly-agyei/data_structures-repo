"""
#getting a substring 

    
        if element in dict, increase value
        else, initialise the key.
        move the right


#changing the substring window
    
    when dict lenght > k: 
    calculate your max from l to r-1: recheck indexing.
    (r-1)-l+1----> max (l,r-1) 
    
    while l < rigtht:
    
        decrement the value of l by one
        if the value become zero:
            remove that element
            break. 
        l+=1 
        
    
    recalculate the max witht the last window 

     
"""
def max_sub(s, k):
    hashh = {}
    max_substring = (0,0,0)
    left, right = 0,0

    while right < len(s):
        if s[right] in hashh:
            s[right] +=1
           
        else:
            s[right] = 1
            
            
            
        #changing the window part
        if len(hashh) > k:
            max_substring = max(max_substring, right-left-1, left, right-1)
            
            #adjust the left
            while len(hashh)>k:
                hashh[s[left]]-=1
                if hashh[s[left]] == 0:
                    del hashh[s[left]] 
                left+=1
                
        right+=1
           
    
    max_substring = max(max_substring, right-left, left, right)
    
    _, left, right = max_substring
    
    
    
    return s[left:right]
        
        
            
              
                
        
        
        
        
    
        
