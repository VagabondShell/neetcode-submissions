class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        saver = {}
        for i in nums:
            if i in saver:
                return True
            else:
                saver[i] = i
        return False
         