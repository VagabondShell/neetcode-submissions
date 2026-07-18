class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l = 0
        r = 0
        uniqChar = set()
        for r in range(len(s)):
            while s[r] in uniqChar:
                uniqChar.remove(s[l])
                l = l + 1
            uniqChar.add(s[r]) 
            maxLen = max(maxLen, len(uniqChar))

        return maxLen