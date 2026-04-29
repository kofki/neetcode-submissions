class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = set(nums)
        return len(found) != len(nums)