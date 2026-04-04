class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        output = []
        
        freq = []
        for key, value in d.items():
            freq.append([value, key])

        freq = sorted(freq)

        while k > 0:
            output.append(freq[-k][1])
            k -= 1

        return output
        