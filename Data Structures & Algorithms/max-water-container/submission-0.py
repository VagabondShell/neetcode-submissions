class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            distance =  right - left
            shortestBar = min(heights[left], heights[right])
            surface = distance * shortestBar
            maxAmount = max(maxAmount, surface)
            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        return maxAmount

