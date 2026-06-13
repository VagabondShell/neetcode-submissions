class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stor = {}
        for i in range(len(nums)):
            temp =  target - nums[i]
            if (temp in stor):
                return [stor[temp], i]
            else:
                stor[nums[i]] = i 
            
        