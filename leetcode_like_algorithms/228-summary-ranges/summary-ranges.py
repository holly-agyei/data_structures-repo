class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        two pointers
        left points to the first element
        right to the next.

        always find the difference btn the right and it's immediate back: if the diff is 1..move on
        if the diff is > 1: record your current interval (left-->right)
        new left = right+1 
        right = left +1 

        

        """
        l,r = 0,0 
        results = []

        while r< len(nums):
            #define conditions
            if r +1 < len(nums) and nums[r+1]-nums[r] < 2:
                r+=1
            else:
                if nums[l] != nums[r]:
                    results.append(f"{nums[l]}->{nums[r]}")
                else: 
                    results.append(f"{nums[l]}")

                if r+1< len(nums):
                    r,l= r+1, r+1
                else: 
                    break
                    
        return results
            






        