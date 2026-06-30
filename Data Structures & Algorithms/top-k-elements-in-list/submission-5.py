class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        res = []
        bucket = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            my_dict[i] = 1 + my_dict.get(i, 0)
        for key, value in my_dict.items():
            bucket[value].append(key)
        for i in range(len(bucket) - 1, 0, -1):
            for element in  bucket[i]:
                res.append(element)
                if len(res) == k:
                    return res