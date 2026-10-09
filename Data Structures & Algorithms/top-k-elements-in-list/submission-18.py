class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # d = {}
        # for num in nums:
        #     if num not in d:
        #         d[num] = 1
        #     else:
        #         d[num] += 1
        
        # freq = sorted(list(d.values()))
        # res = []
        # for i in range(-k, 0):
        #     for k, v in d.items():
        #         if freq[i] == v and k not in res:
        #             res.append(k)

        # return res

        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        count = [[] for i in range(len(nums) + 1)]
        
        for n, c in d.items():
            count[c].append(n)

        output = []
        for i in range(len(count)-1, 0, -1):
            for j in count[i]:
                output.append(j)
                if len(output) == k:
                    return output
        
        

