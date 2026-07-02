class Solution:

    def encode(self, strs: List[str]) -> str:
        result_list = []
        for w in strs:
            result_list.append(f"{len(w)}#{w}")
        return "".join(result_list) 

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 
        j = 0  
        
        while i < len(s):
            if s[i] == '#':
                num = int(s[j:i])
                word = s[i + 1:i + 1 + num]
                result.append(word)
                i = i + 1 + num
                j = i 
            else:
                i += 1
                
        return result
