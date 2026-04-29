class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT = {}
        window = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)

        l = 0

        res = [-1, -1]
        resLen = float('inf')

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(s[r], 0) + 1

            if c in countT and countT[c] == window[c]:
                have += 1
        
            while have == need:
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l+= 1
        return s[res[0]: res[1]+1] if resLen != float('inf') else ""





