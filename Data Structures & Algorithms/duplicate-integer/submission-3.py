class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for val in nums:
            if val in freq:
                return True
            else:
                freq[val] = 1

        return False
        