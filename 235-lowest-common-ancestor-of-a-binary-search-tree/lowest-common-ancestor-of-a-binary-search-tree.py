# 

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        pathofp = []
        pathofq = []
        self.findPath(root, p, pathofp)
        self.findPath(root, q, pathofq)
        i = 0
        lca = None
        while i< len(pathofp) and i < len(pathofq):
            if pathofp[i] == pathofq[i]:
                lca = pathofp[i]
            else:
                break
            i = i+1
        return lca
    def findPath(self, root, target, path):
        #brute force
        if root is None:
            return False
        path.append(root)
        if root.val == target.val:
            return True
        if self.findPath(root.left, target, path):
            return True
        if self.findPath(root.right, target, path):
            return True
        path.pop()
        return False
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root



     