class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        maxAmount = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = r + 1
            else:
                diff = prices[r] - prices[l]
                maxAmount = max(maxAmount, diff)
                r = r + 1
        return maxAmount
