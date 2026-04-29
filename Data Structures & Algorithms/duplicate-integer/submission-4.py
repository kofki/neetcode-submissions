class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing = set(nums)
        return len(existing) != len(nums)