class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a heapq, or just sort?
        # Counter = O(N), sorting is O(log n)
        count = Counter(nums)
        sorted_nums = sorted(count.items(), key=lambda x: -x[1])[:k]
        res = [num[0] for num in sorted_nums]
        return res
