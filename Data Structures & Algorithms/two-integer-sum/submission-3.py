class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, num in enumerate(nums):
            if num not in s:
                s[target-num] = i
            else:
                return [s[num], i]