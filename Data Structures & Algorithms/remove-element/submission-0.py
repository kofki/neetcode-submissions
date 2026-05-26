from collections import deque
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = deque()
        count = 0
        for i, num in enumerate(nums):
            if num == val:
                s.append(i)
                continue
            
            count += 1
            if s:
                nums[s.popleft()] = num
                s.append(i)
        return count