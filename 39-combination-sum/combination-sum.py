class Solution(object):
    def combinationSum(self, candidates, target):
        results = []
        def backtrack(remain, current_combination, start_index):
            if remain == 0:
                results.append(list(current_combination))
                return
            if remain < 0:
                return
            for i in range(start_index, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(remain - candidates[i], current_combination, i)
                current_combination.pop()
        backtrack(target, [], 0)
        return results

  

        