class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                k = j + 1
                while k < len(nums):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        insert = sorted([nums[i], nums[j], nums[k]])
                        if insert not in output:
                            output.append(insert)
                    k += 1
                j += 1
            i += 1

        return output