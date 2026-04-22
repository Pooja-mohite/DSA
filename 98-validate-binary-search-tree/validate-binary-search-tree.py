# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        #brute force
        def checkleft(node, value):
            if node is None:
                return True
            if node.val >= value:
                return False
            return checkleft(node.left, value) and checkleft(node.right, value)
        
        def checkright(node, value):
            if node is None:
                return True
            if node.val <= value:
                return False
            return checkright(node.left, value) and checkright(node.right, value)
        
        def check(node):
            if node is None:
                return True
            if not checkleft(node.left, node.val):
                return False
            if not checkright(node.right, node.val):
                return False
            return check(node.left) and check(node.right)
        return check(root)

            
                
        
