class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        words = set()
        max_run = 0
        l = 0
        for r in range(len(s)):
            while s[r] in words:
                words.remove(s[l])
                l+= 1
            words.add(s[r])
            max_run = max(max_run, r - l + 1)
        return max_run
