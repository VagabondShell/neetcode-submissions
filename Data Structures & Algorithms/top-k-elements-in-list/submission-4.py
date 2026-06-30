class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        #then create the backet aproach then return it 
        lent = len(nums)
        bucket = [[] for _ in range(lent + 1)] 
        for key, value in my_dict.items():
            bucket[value].append(key)
        res = []
        while lent >= 0 and len(res) < k:
            if len(bucket[lent]) > 0:
                for element in  bucket[lent]:
                    res.append(element)
                    if len(res) == k:
                        return res
            lent -= 1
        return res