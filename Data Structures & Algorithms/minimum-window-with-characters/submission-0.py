from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hach = dict(Counter(t))
        l = 0
        r = 0
        satifated = 0
        lenght = len(hach)
        bestLenght = float("inf")

        for r in range(len(s)):
            if s[r] in hach:
                hach[s[r]] = hach[s[r]] - 1
                if hach[s[r]] == 0:
                    satifated = satifated + 1

            while satifated == lenght:
                currentLenght = r - l + 1
                if currentLenght < bestLenght:
                    bestLenght = currentLenght
                    position = l

                if s[l] in hach:
                    hach[s[l]] = hach[s[l]] + 1
                    if hach[s[l]] > 0:
                        satifated = satifated - 1
                l = l + 1
        if bestLenght == float("inf"):
            return ""
        return s[position : position + bestLenght]
