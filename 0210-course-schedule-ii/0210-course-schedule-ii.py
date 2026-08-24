from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for course, preq in prerequisites:
            graph[preq].append(course)
            indegree[course] += 1
        
        # 1. FIXED: Initialize as a deque so popleft() works
        ready_to_do = deque() 
        for course in range(numCourses):
            if indegree[course] == 0:
                # 2. FIXED: Use () for append instead of []
                ready_to_do.append(course) 
                
        schedule = []

        while ready_to_do:
            # 3. FIXED: Add () to call the function
            course = ready_to_do.popleft() 
            schedule.append(course)

            for neighbor in graph[course]:
                # 4. FIXED: Typo in "neighbor"
                indegree[neighbor] -= 1 
                if indegree[neighbor] == 0:
                    ready_to_do.append(neighbor)

        # 5. ADDED: The final check for a valid schedule!
        if len(schedule) == numCourses:
            return schedule
        else:
            return []