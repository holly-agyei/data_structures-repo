class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                popped = stack.pop()
                next_greater[popped] = num
            stack.append(num)

        # now just lookup the answer for each num in nums1
        return [next_greater.get(num, -1) for num in nums1]



        

        







        




        