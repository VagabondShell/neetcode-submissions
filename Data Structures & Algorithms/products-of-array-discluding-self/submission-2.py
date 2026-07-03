class Solution:
    def productExceptSelf(self, nums):
        lent = len(nums)
        
        # Pre-allocate arrays
        prefix = [1] * lent
        suffix = [1] * lent
        result = [1] * lent

        # Build "Strictly Before" array
        for i in range(1, lent):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Build "Strictly After" array (counting backward)
        for i in range(lent - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Multiply them directly together
        for i in range(lent):
            result[i] = prefix[i] * suffix[i]

        return result