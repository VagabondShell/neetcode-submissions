class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hold = {}
        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')] += 1
            tuple_count = tuple(count)
            if tuple_count not in hold:
                hold[tuple_count] = []
            hold[tuple_count].append(w)
        return list(hold.values())