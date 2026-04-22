# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        #brute force(dfs- recursive)
        """
        result = []
        def dfs(node, level):
            if node is None:
                return
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)
        return result
        """
        # optimized(BFS - QUEUE)
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            level = []
            size = len(queue)
            i = 0
            while i<size:
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                i = i+1
            result.append(level)
        return result

