# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # brutte force
    '''
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)

        return 1 + max(left, right)
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)

        currentdiameter = leftheight + rightheight

        leftdiameter = self.diameterOfBinaryTree(root.left)
        rightdiameter = self.diameterOfBinaryTree(root.right)

        return max(currentdiameter, leftdiameter, rightdiameter)
        '''
        #dfs
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.diameter

    
    
        