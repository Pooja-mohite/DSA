class Solution(object):
    def permute(self, nums):
        n = len(nums)
        result = []
        current = []
        visited = [False] * n
        def backtrack():
            if len(current) == n:
                result.append(current[:])
                return
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                current.append(nums[i])
                backtrack()
                current.pop()
                visited[i] = False
        backtrack()
        return result





        
        
        