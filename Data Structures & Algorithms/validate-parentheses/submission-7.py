class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c not in bracket_map:
                stack.append(c)
            elif not stack:
                return False
            elif bracket_map[c] == stack[-1]:
                stack.pop()
            else:
                return False
        if not stack:
                return True
        else:
            return False
