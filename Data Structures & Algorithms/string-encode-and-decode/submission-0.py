class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for w in strs:
            length = len(w)
            encoded_string = f"{length}#{w}"
            result += encoded_string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        l = 0
        r = 0   
        while r < len(s):
            if s[r] == '#':
                num = int(s[l:r])
                word = s[r + 1: (r + 1) + num]
                result.append(word)
                r += num + 1
                l = r
            else:
                r += 1
        return result

