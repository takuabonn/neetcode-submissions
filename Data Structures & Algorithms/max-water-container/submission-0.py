class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        maxS = 0
        while l < r:
            lh = heights[l]
            rh = heights[r]
            maxS = max(maxS, min(lh, rh)*(r - l))
            if lh < rh:
                l += 1
                continue
            if rh < lh:
                r -= 1
                continue
            l += 1
        
        return maxS
        
