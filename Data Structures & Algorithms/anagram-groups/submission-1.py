from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        my_dict = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            my_dict[sorted_word].append(word)
    
        return list(my_dict.values())