class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val  = 0
        left = 0
        right = 1
        while left < len(prices) and right < len(prices): 
            if (prices[left] < prices[right]):
                temp = prices[right] - prices[left]
                if temp > max_val:
                    max_val = temp
                right += 1
            else:
                left = right
                right += 1
            
        return max_val