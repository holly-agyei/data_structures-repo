class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        
        ans = [-1] * len(nums2)
        stack = []
        real_ans = [-1] * len(nums1)

        for index, num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                ans[stack[-1]] = num
                stack.pop()
            stack.append(index)

        for i, num in enumerate(nums2):
            if num in nums1:
                real_ans[nums1.index(num)] = ans[i]

        return real_ans




        

        







        




        