class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if i < len(s):
                    if s[i] != c:
                        return res
                else:
                    return res
            res += c
        return res
                
                    
