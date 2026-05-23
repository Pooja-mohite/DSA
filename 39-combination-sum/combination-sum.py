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
                curr_num = candidates[i]
                path.append(curr_num)
                dfs(i, path, total + curr_num)
                path.pop()
                i = i+1
        dfs(0,[],0)
        return result



            