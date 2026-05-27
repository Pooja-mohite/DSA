# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        '''
        # bfs
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth = depth + 1
        return depth
        '''
        # dfs

        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
        
       
        
        