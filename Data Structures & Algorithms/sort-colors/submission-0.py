class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = Counter(nums)
        current_color = 0
        for i in range(len(nums)):
            if colors[current_color] > 0:
                nums[i] = current_color
            else:
                while colors[current_color] <= 0:
                    current_color += 1
                nums[i] = current_color
            colors[current_color] -= 1
        