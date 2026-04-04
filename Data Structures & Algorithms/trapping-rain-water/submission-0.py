class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxL = height[l]
        maxR = height[r]

        water = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                diff = min(maxL, maxR) - height[l]
                if diff > 0:
                    water += diff

            else:
                r -= 1
                maxR = max(maxR, height[r])
                diff = min(maxL, maxR) - height[r]
                if diff > 0:
                    water += diff

        return water