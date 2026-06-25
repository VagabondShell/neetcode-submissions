class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val  = 0
        left = 0
        right = 1
        while right < len(prices): 
            if (prices[left] < prices[right]):
                max_val = max(max_val, prices[right] - prices[left])
            else:
                left = right
            right += 1
            
        return max_val