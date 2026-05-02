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
            #create new node
            newnode = Node(oldnode.val)

            #copy connections
            for neighb in oldnode.neighbors:
                newnode.neighbors.append(dfs(neighb))
            return newnode
        return dfs(node) 
        """
        #optimized
        
        visited = {}
        if node is None:
            return None
        def dfs(oldnode):
            if oldnode in visited:
                return visited[oldnode]
            new_node = Node(oldnode.val)
            visited[oldnode] = new_node
            for neighbor in oldnode.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node)
            

