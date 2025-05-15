class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda x: x[1])

        prev_end = float("-inf")
        balloons = 0

        for interval in points[:]:
            if interval[0]>prev_end: #keep
                prev_end = interval[1]
                balloons+=1
                
            
                
        return balloons #bassically checkingn the number of overlaps

        #I love greedy approach! to use greeedy approach, alway take the question to real life scenario and think differently.
        #get a hypothesis with a guarantee that it works. 



