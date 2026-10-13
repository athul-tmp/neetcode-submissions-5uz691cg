class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)

        longest = 0

        for i in setNums:
            currLongest = 0
            if i - 1 not in setNums:
                num = i
                while num in setNums:
                    currLongest += 1
                    num += 1
                longest = max(currLongest, longest)
                
        return longest

