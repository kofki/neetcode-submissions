class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i, first in enumerate(nums):
            if first > 0:
                break

            if i > 0 and first == nums[i - 1]:
                continue

            l = i+ 1
            r = n -1
            while l < r:
                res = first + nums[l] + nums[r]
                if res < 0:
                    l += 1
                elif res > 0:
                    r -= 1
                else:
                    ans.append([first, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return ans
        