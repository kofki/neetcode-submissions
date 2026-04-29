class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        while l < r:
            res = target - numbers[l] - numbers[r]
            if res > 0:
                l += 1
            elif res < 0:
                r -= 1
            else:
                return [l+1, r+1]