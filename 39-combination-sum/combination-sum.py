class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        def dfs(start, path, sum):
            if sum == target:
                result.append(path[:])
                return
            if sum > target:
                return
            i = start
            while i < len(candidates):
                curr_num = candidates[i]
                path.append(curr_num)
                dfs(i, path, sum+curr_num)
                path.pop()
                i = i+1
        dfs(0,[],0)
        return result
        