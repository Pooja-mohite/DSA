class Solution(object):
        def topKFrequent(self, nums, k):
            count = {}
            for n in nums:
                count[n] = 1 + count.get(n, 0)
            buckets = [[] for _ in range(len(nums) + 1)]
            for num, freq in count.items():
                buckets[freq].append(num)
            res = []
            for i in range(len(buckets) - 1, 0, -1):
                for n in buckets[i]:
                    res.append(n)
                    if len(res) == k:
                        return res