class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: list of strings
        # output: list of list of strings
        # organize the strings into boxes, if the boxes are the same, store string there
        # boxes have to be the exact same. Use a list of the numerical value of the char as index
        res = defaultdict(list)
        for s in strs:
            box = [0] * 26
            for c in s:
                box[ord(c) - ord('a')] += 1
            res[tuple(box)].append(s)
        return list(res.values())