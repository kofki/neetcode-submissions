class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        n = len(nums)
        r = []
        for k, v in c.items():
            if v > n // 3:
                r.append(k)
        return r