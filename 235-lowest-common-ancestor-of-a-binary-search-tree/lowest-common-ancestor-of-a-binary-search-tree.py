# 

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        #Brute Force
        '''
        p_path = []
        q_path = []
        self.findpath(root, p_path, p)
        self.findpath(root, q_path, q)
        i = 0
        lowestrancestor = None
        while i < len(p_path) and i < len(q_path):
            if p_path[i] == q_path[i]:
                lowestancestor = p_path[i]
            else:
                break
            i = i+1
        return lowestancestor
                                                                                             
    def findpath(self, root, path, target):
        if root is None:
            return False
        path.append(root)
        if root.val == target.val:
            return True
        if self.findpath(root.left, path, target):
            return True
        if self.findpath(root.right, path, target):
            return True
        path.pop()
        return False
        '''
        #optimized
        while root:
            if p.val < root.val and q.val< root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root= root.right
            else:
                return root
        