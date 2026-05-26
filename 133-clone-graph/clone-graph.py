"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        # BRute force
        """
        if not node:
            return None
        def dfs(old_node):
            newnode = Node(old_node.val)
            for neighbor in old_node.neighbors:
                newnode.neighbors.append(dfs(neighbor))
            return newnode
        return dfs(node)
        """
        visited = {}
        def dfs(old_node):
            if not node:
                return None
            if old_node in visited:
                return visited[old_node]
            else:
                newnode = Node(old_node.val)
                visited[old_node] = newnode
                for neighbor in old_node.neighbors:
                    newnode.neighbors.append(dfs(neighbor))
                return newnode
        return dfs(node)








       
        

            






       
    
        

                

        
        