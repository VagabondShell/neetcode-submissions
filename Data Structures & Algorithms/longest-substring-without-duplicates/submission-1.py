class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        dic = {}
        left = 0
        right = 0
        maxSize = 0
        while right < len(s):
            if s[right] in dic and dic[s[right]] >= left:
                left = dic[s[right]] + 1
                dic[s[right]] = right
            dic[s[right]] = right
            maxSize = max(maxSize, right - left + 1) 
            right += 1
        return maxSize
