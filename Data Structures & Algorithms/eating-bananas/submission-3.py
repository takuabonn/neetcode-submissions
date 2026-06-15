class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1, max(piles)

        k = right
        while left <= right:
            mid = left + ((right-left)//2)
            remain = h
            for p in piles:
                remain -= (p+(mid-1))//mid
            if remain >= 0:
                k = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return k
        


            
