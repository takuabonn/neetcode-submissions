class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1, max(piles)

        k = right
        while left <= right:
            mid = left + ((right-left)//2)
            remain = h
            for p in piles:
                remain -= ((-1 * p)//mid)*-1
            if remain >= 0:
                k = mid
                right = mid - 1
            elif remain < 0:
                left = mid + 1
            
        return k
        


            
