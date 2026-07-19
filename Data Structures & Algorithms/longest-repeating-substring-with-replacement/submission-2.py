class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        longestSub = 0
        l = 0
        r = 0
        while r < len(s):
            dic[s[r]] = dic.get(s[r], 0) + 1
            lenght = r - l + 1
            largestKey = max(dic.values())
            cheker = lenght - largestKey
            if cheker > k:
                dic[s[l]] = dic[s[l]] - 1
                l = l + 1
            else:
                longestSub = max(longestSub, lenght)
            r = r + 1
        return longestSub
