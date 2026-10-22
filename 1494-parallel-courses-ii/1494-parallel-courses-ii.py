from functools import lru_cache
from itertools import combinations

class Solution:
    def minNumberOfSemesters(self, n: int, relations: list[list[int]], k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        prerequisites = {i: set() for i in range(1, n + 1)}

        for pre, course in relations:
            graph[pre].append(course)
            prerequisites[course].add(pre)

        @lru_cache(None)
        def explore(completed):
            # completed is a frozenset

            if len(completed) == n:
                return 0

            available = []

            # Find all courses we can take now
            for course in range(1, n + 1):
                if course in completed:
                    continue

                # All prerequisites must already be completed
                if prerequisites[course].issubset(completed):
                    available.append(course)

            # If we can take all available courses, take them
            if len(available) <= k:
                new_completed = set(completed)

                for course in available:
                    new_completed.add(course)

                return 1 + explore(frozenset(new_completed))

            # Otherwise, try every possible group of k courses
            best = float("inf")

            for chosen in combinations(available, k):
                new_completed = set(completed)

                for course in chosen:
                    new_completed.add(course)

                semesters = 1 + explore(frozenset(new_completed))

                best = min(best, semesters)

            return best

        return explore(frozenset())