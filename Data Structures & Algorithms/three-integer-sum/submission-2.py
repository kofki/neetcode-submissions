class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        for i, first in enumerate(nums):
            l = i+ 1
            r = n -1
            while l < r:
                res = first + nums[l] + nums[r]
                if res < 0:
                    l += 1
                elif res > 0:
                    r -= 1
                else:
                    ans.add((first, nums[l], nums[r]))
                    l += 1
                    r -= 1
        return [list(tup) for tup in ans]
        