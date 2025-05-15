class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        #initialise results to empty arr
        res = []
        #initialise the most recent bin value
        bin_val = -1

        for index, value in enumerate(groups):
            #greedy: try to form as many alternation as u can 
            if value != bin_val:
                res.append(words[index])
                bin_val = value
        
        return res


        