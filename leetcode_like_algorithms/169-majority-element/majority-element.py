class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count ==0:
                candidate = num
            if num== candidate:
                count+=1
            elif num != candidate:
                count-=1
        return candidate
        

        

        