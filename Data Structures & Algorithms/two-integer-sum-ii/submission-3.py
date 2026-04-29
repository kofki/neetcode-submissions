class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = {}
        for index, num in enumerate(numbers):
            if not num in complement:
                complement[target-num] = index
            else:
                return [complement[num]+1, index+1] if num > target-num else [index+1, complement[num]+1]