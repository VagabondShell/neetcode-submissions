class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, w in enumerate(nums):
            if i > 0 and w == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sumIndex = w + nums[l] + nums[r] 
                if sumIndex == 0:
                    res.append([w, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif sumIndex < 0:
                    l += 1
                else:
                    r -= 1
                
            
        return res