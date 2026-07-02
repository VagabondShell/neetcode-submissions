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
                word_start = i + 1
                word_end = word_start + num
                word = s[word_start:word_end]
                result.append(word)
                i = word_end
                j = i 
            else:
                i += 1
                
        return result
