class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq_map = {}
        max_length = 0 
        l =0

        for r in range(len(nums)):
            #make sure the sub_array is good
            freq_map[nums[r]] = freq_map.get(nums[r], 0)+1 

            while freq_map[nums[r]] and freq_map[nums[r]]>k:
                freq_map[nums[l]]-=1 
                if freq_map[nums[l]]<=0:
                    del freq_map[nums[l]]
                l+=1 
            max_length = max(r-l+1, max_length)
        
        return max_length
            

           



        