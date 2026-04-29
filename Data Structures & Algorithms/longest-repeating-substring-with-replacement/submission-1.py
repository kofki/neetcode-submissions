class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # make a sliding window, where I track and make sure that the maxfrequency is recorded
        # if the window needs more replacements (is invalid), then shorten it (move left pointer) and update frequencies
        res = 0
        count = {}

        maxF = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            while r - l + 1 - maxF > k:
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res