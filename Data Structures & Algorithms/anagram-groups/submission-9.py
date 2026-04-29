class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # traverse through list, if find anagram previously found, store in a dictionary
        # probably sort to the anagram as the key?
        anagrams = {}
        for s in strs:
            anagram = tuple(sorted(s))
            if anagram in anagrams:
                anagrams[anagram].append(s)
            else:
                anagrams[anagram] = [s]
        return list(anagrams.values())
