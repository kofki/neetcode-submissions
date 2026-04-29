class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # input array nums, if the unique nums is less than total nums then has duplicate
        return len(set(nums)) != len(nums)