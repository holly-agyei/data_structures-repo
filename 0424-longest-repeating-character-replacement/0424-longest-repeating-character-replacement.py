class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #chars to change = window len - MaxFreq 

        freq_map, max_freq, left, right = {}, 0, 0, 0 
        max_len = 0 #best window len found

        for right in range(len(s)):
            r_char = s[right] 
            #update the count in the freq 
            freq_map[r_char] = freq_map.get(r_char, 0)+1
            #update the max_freq in the window 
            max_freq = max(max_freq, freq_map[r_char])
            window_len = right-left+1 
            
            #if the chars to replace > k: shrink
            if window_len-max_freq >k:
                l_char = s[left]
                freq_map[l_char]-=1 #dont delete when it's zero cox u dey use the .get up there
                left+=1

            max_len = max(right-left+1, max_len)
        
        return max_len



         