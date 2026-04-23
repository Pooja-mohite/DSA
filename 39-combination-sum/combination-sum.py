class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        def dfs(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            i = start
            while i < len(candidates):
                num = candidates[i]
                #choose
                path.append(num)
                #explore
                dfs(i, path, total + num)
                #backtrack
                path.pop()
                #next no. try
                i = i+1
        dfs(0, [], 0)
        return result
    