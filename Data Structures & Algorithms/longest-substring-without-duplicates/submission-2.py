class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0
        hold = set()
        for r in range(len(s)):
            while s[r] in hold:
                hold.remove(s[l])
                l += 1
            hold.add(s[r])
            count = max(count, (r - l) + 1)
        return count