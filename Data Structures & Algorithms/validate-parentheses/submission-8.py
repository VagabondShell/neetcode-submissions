class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c not in bracket_map:
                stack.append(c)
            elif not stack or bracket_map[c] != stack[-1]:
                return False
            else:
                stack.pop()
        if not stack:
                return True
        return False
