# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        # brute force
        self.maxsum = root.val
        def dfs(node):
            if node is None:
                return 0
            #left sum
            left = dfs(node.left)

            #right sum
            right = dfs(node.right)

            # ignore if negatiive
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            
            #full path (node as middle)
            current_sum = left + node.val + right
            #max update
            if current_sum > self.maxsum:
                self.maxsum = current_sum
            
            return node.val + max(left, right)

        dfs(root)
        return self.maxsum

