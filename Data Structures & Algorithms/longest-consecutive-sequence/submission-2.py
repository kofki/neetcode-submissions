class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ordered = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in ordered:
                length = 0
                while (n+ length) in ordered:
                    length += 1
                longest = max(longest, length)
        return longest