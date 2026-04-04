class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        volumes = []

        while i < j:
            water = (j-i) * min(heights[i],heights[j])
            volumes.append(water)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max(volumes)
