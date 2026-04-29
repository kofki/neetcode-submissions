class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find pairs that match target
        # brute force, find match per each character O(n^2)
        # O(n), Use a hash map of target
        targets = {}
        for index, num in enumerate(nums):
            if num in targets:
                return [targets[num], index]
            targets[target-num] = index
        