class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # matematically if the next lexicographical is when there is the first instance
        # where nums[i] < nums[i+1] and if there is any space for more later down the line
        # keep going until strictly descending since pivot and then move pivot left
        n = len(nums)
        i = n -2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        l, r = i+ 1, n-1
        while l <r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -=1
            