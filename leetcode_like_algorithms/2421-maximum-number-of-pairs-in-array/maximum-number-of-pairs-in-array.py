class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        """
        -choose 2 equal integers
        -remove them
        answer size 2[number of pairs, left overs in the array]

        """
        #count the numbers and freq
        #for any key with freq >=2:
            #count_pair = key//2
            #count_rem = val%2
        val_freqs = Counter(nums)
        index1=0
        index2 =0
        for value in val_freqs.values():
            index1 = index1+(value//2)
            index2 = index2 +(value%2)
        
        return [index1, index2]