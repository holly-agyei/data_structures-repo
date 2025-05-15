class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #greedy approach 
        """
        this is greedy approach. we want to sort them in order of which meeting finished early x[1]
        and have more spaced for future meetings. any meeting that overlaps with the one which ended early( started before the one
        the one that ended early to end) should be removed.--> probbly started late. 



        """
        intervals.sort(key = lambda x: x[1])

        prev_end = float("-inf")
        overlaps = 0

        for interval in intervals[:]:
            if interval[0]>=prev_end: #keep
                prev_end = interval[1]
            else: #remove that meeting an go to the next that ended late, check if it didnt overlap with the prev end.
                overlaps+=1
        return overlaps #bassically checkingn the number of overlaps

        #I love greedy approach! to use greeedy approach, alway take the question to real life scenario and think differently.
        #get a hypothesis with a guarantee that it works. 





