class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        numSet = set(sortedNums)
        longest = 0

        for num in numSet:
            length = 1
            while (num + length) in numSet:
                length += 1
            longest = max(length, longest)

        return longest