class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = {}

        for i in nums:
            key = i
            if key not in res:
                res[key] = 1
            else:
                res[key] = res.get(key) + 1

        return list(dict(sorted(res.items(), key = lambda x:x[1], reverse = True)).keys())[:k]
        