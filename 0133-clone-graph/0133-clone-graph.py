from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        stack = [node]
        copy = {node: Node(node.val)}
        
        while stack:
            curr = stack.pop()
            
            for neighbor in curr.neighbors:
                if neighbor not in copy:
                    copy[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                    
                copy[curr].neighbors.append(copy[neighbor])
                
        return copy[node]