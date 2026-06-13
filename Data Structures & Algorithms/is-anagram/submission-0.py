class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = {}
        if (sorted(s) == sorted(t)):
            return True
        return False