class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        inventory = {}
        for num in nums:
            if num in inventory:
                return True
            else:
                inventory[num] = 1
        return False