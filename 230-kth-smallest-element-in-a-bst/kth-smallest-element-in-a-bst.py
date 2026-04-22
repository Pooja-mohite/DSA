# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        #brute force
        """
        result = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result[k-1]
        """

        #optimized
        self.count = 0
        self.ans = 0
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.count = self.count + 1
            if self.count == k:
                self.ans = node.val
                return
            inorder(node.right)
        inorder(root)
        return self.ans


        

        