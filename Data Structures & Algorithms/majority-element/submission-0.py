class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        res = Counter(nums)
        return res.most_common(1)[0][0]