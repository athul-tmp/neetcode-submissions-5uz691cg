class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        answer = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in d:
                answer.append(d[difference])
                answer.append(i)
            else:
                d[nums[i]] = i
        
        return answer