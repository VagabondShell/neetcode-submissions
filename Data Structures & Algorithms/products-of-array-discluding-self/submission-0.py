class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        prefix[0] = nums[0]
        suffix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]


        for i in range(len(nums) - 2 , -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(suffix[i + 1])
            elif i == len(nums) - 1:
                result.append(prefix[i - 1])
            else:
                result.append(suffix[i + 1] * prefix[i - 1])

        return result


        