class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        freq = sorted(list(d.values()))
        res = []
        for i in range(-k, 0):
            for k, v in d.items():
                if freq[i] == v and k not in res:
                    res.append(k)

        return res