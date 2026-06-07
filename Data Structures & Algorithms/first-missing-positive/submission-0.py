class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        found = set()
        ans = 1
        for num in nums:
            found.add(num)
        while ans in found:
            ans += 1
        return ans