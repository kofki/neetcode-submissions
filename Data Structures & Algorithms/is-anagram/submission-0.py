from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = Counter(s)
        l2 = Counter(t)
        return l1 == l2