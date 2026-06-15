class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {num: index for index, num in enumerate(nums)}
        for i in range(len(nums)):
            target_value = target - nums[i]
            if target_value in index_map:
                index = index_map[target_value]
                if i != index:
                    return [i, index]
