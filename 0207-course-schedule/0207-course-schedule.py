from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        can_do = deque()

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1

        for idx, num in enumerate(indegrees):
            if num == 0:
                can_do.append(idx)

        count = len(can_do)

        while can_do:
            course = can_do.popleft()

            for nei in graph[course]:
                indegrees[nei] -= 1

                if indegrees[nei] == 0:
                    can_do.append(nei)
                    count += 1

        return count == numCourses