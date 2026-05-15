"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        if not node:
            return None
        def dfs(oldnode):
            newnode = Node(oldnode.val)
            for neighbor in oldnode.neighbors:
                newnode.neighbors.append(dfs(neighbor))
            return newnode
        return dfs(node)
        """
        visited = {}
        if not node:
            return None
        def dfs(oldnode):
            if oldnode in visited:
                return visited[oldnode]
            else:
                newnode = Node(oldnode.val)
                visited[oldnode] = newnode
                for neighbor in oldnode.neighbors:
                    newnode.neighbors.append(dfs(neighbor))
                return newnode
        return dfs(node)


            






       
    
        

                

        
        