class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count the characters, they have to match
        return Counter(s) == Counter(t)