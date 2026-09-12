class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        allowed = []
        not_allowed = set()
        parent = {}
        def parser(string):
            if "".join([string[1], string[2]]) == "==":
                allowed.append([string[0], string[3]])
            else:
                not_allowed.add((string[0], string[3]))
            if string[0] not in parent:
                parent[string[0]] = string[0]
            if string[3] not in parent:
                parent[string[3]] = string[3]
            
        
        for equation in equations:
            parser(equation)
        
        def find(node):
            path = []
            while parent[node] != node:
                path.append(node)
                node = parent[node]
            top_boss = node
            for a in path:
                parent[a] = top_boss
            return top_boss
        for u,v in allowed:
            bossu = find(u)
            bossv = find(v)
            
            parent[bossv]=bossu 
        for u,v in not_allowed:
            bossu = find(u)
            bossv = find(v)
            if bossu==bossv:
                return False 
            
        return True

        



        