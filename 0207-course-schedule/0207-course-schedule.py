from collections import defaultdict 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        #first build a graph of course and their prerequisites a->b where a is pre of b
        that's actually list cox this is a directed graph. a mapping to b, direction is important

        """
        nodes = set()
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
            nodes.add(u)
            nodes.add(v)
       
        #now we are gonna use stacks for this
        #since there can be disconnection in the dag
        visited = set()
        instack = set()

        for node in nodes:
            if node in visited:
                continue
            stack = [(node, 0)]
            while stack:
                node, state = stack.pop()
                if state == 1:
                    instack.discard(node)
                    continue
                # if node in visited:
                #     continue
                stack.append((node,1))
                instack.add(node)
                visited.add(node)

                for nei in graph[node]:
                    if nei not in visited:
                        stack.append((nei,0))
                    elif nei in instack:
                        return False
        return True



                







        