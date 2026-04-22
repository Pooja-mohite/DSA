# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    def isSubtree(self, root, subRoot):
        
        if root is None:
            return False
        if self.isSametree(root, subRoot):
            return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right
    def isSametree(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)
        """
    def serialize(self, root):
        if root is None:
            return 'null,'
        return "#" + str(root.val) + "," + \
            self.serialize(root.left) + \
            self.serialize(root.right)
    def isSubtree(self, root, subRoot):
        root_string = self.serialize(root)
        subRoot_string = self.serialize(subRoot)
        return subRoot_string in root_string

           