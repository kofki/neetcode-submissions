class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mode = Counter(nums)
        topk, freq = zip(*sorted(mode.items(), key=lambda x: -x[1]))
        return list(topk)[:k]