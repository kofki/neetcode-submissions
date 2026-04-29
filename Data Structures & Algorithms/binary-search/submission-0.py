class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) -1
        while min <= max:
            guess = min + ((max - min)//2)
            if nums[guess] < target:
                min = guess +1
            elif nums[guess] > target:
                max = guess -1
            else:
                return guess
        return -1