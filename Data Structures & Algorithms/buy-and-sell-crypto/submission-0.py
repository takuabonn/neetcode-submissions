class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        result = 0
        while r <= len(prices)-1:
            p = prices[r]-prices[l]
            result = max(result, p)
            if p < 0:
                l = r
            r = r + 1
        return result





