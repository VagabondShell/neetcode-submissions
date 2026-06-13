from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angram = defaultdict(list)
        result = []
        for s in strs:
            temp = tuple(sorted(s))
            angram[temp].append(s)
        for value in angram.values():
            result.append(value)
        return result
