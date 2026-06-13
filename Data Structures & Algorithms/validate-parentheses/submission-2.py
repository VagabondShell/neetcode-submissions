class Solution:
    def isValid(self, s: str) -> bool:
        dec = {")":"(", "]":"[", "}":"{"}
        stack = []
        for a in s:
            if a in dec:
                if stack and stack[-1] == dec[a]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(a)
        if not stack:
            return True
        else:
            return False
