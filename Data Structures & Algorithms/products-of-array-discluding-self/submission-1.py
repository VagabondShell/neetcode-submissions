class Solution:
    def productExceptSelf(self, nums):
        lent = len(nums)
        prefix = [1] * lent
        suffix = [1] * lent

        prefix[0] = nums[0]
        suffix[lent - 1] = nums[lent - 1]

        for i in range(1, lent):
            prefix[i] = prefix[i - 1] * nums[i]

        for i in range(lent - 2 , -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        result = []
        
        for i in range(lent):
            if i == 0:
                result.append(suffix[i + 1])
            elif i == lent - 1:
                result.append(prefix[i - 1])
            else:
                result.append(suffix[i + 1] * prefix[i - 1])
        return result




        