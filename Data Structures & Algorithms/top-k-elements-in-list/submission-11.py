class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a heapq, or just sort?
        # Counter = O(N), sorting is O(n*log n)
        # bucket sort, where the frequency is the index
        counter = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]
        for num, cnt in counter.items():
            buckets[cnt].append(num)
        
        res = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        