class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for s in strs:
            v = "".join(sorted(s))
            if v in a:
                a[v].append(s)
            else:
                a[v] = [s]
        return list(a.values())